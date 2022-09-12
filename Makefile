pull:
	@docker compose pull

up:
	@docker compose up -d

down:
	@docker compose down

ps:
	@docker compose ps

logs:
	@docker compose logs -f

start:
	@open "http://localhost:8888"

enter:
	@docker compose exec -it glue bash
