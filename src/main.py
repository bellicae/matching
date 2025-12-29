from src.services.data_loader import DataLoader
from src.services.filter_engine import FilterEngine
from src.models.player_filter import PlayerFilter
from src.services.quote_service import QuoteService
from src.models.quote_request import QuoteRequest
from src.models.quote_response import QuoteResponse
from utils import generate_unique_id, format_currency

def main():
    # ----------------------------
    # 1️⃣ Load hosts
    # ----------------------------
    data_loader = DataLoader("data")
    hosts = data_loader.load_hosts()
    print(f"{len(hosts)} hosts loaded.")

    # ----------------------------
    # 2️⃣ Define player filter
    # ----------------------------
    player_filter = PlayerFilter(
        races=["Ranger", "Warrior"],  # LARP races
        required_services=["fantasy", "forest"],
        require_included_services=True,
        max_rate=200,
        required_costume="Elf Warrior",
        allow_custom_costume=True,
        max_custom_costume_price=60
    )

    # ----------------------------
    # 3️⃣ Filter hosts
    # ----------------------------
    matching_hosts = FilterEngine.filter_hosts(hosts, player_filter)
    print(f"{len(matching_hosts)} matching hosts found:")
    for host in matching_hosts:
        print(f"- {host.name} ({host.race}) - {format_currency(host.base_rate)}/hr")

    # ----------------------------
    # 4️⃣ Initialize quote service
    # ----------------------------
    quote_service = QuoteService("data")

    # ----------------------------
    # 5️⃣ Create a quote request for the first matching host (example)
    # ----------------------------
    if matching_hosts:
        selected_host = matching_hosts[0]
        request_id = generate_unique_id("qr")
        new_request = QuoteRequest(
            request_id=request_id,
            player_id="player001",
            host_id=selected_host.host_id,
            character_name="Dragon Knight",
            details="Need full armor and props ready in 2 weeks"
        )
        quote_service.add_quote_request(new_request)
        print(f"\nQuote request created for {selected_host.name} with ID: {request_id}")

        # ----------------------------
        # 6️⃣ Host responds (example)
        # ----------------------------
        response = QuoteResponse(
            request_id=request_id,
            quoted_price=75,
            estimated_time_days=14,
            notes="Costume available, dragon props included"
        )
        quote_service.add_quote_response(response)
        print(f"Quote response saved: {format_currency(response.quoted_price)} in {response.estimated_time_days} days")

        # ----------------------------
        # 7️⃣ Retrieve all responses for the request
        # ----------------------------
        responses = quote_service.get_responses_for_request(request_id)
        print(f"\nResponses for request {request_id}:")
        for r in responses:
            print(f"- {format_currency(r.quoted_price)} in {r.estimated_time_days} days | Notes: {r.notes}")
    else:
        print("No hosts matched your filter criteria.")


if __name__ == "__main__":
    main()
