from dslResolver.DSLResolver import DSLResolver

class BankResolver(DSLResolver):
    # Defining constants
    RESOLVER_KEYWORD = "bank"
    INTEREST = "interest"
    TARGET_DONE = "target_done"

    def get_resolver_keyword(self) -> str:
        return self.RESOLVER_KEYWORD

    def resolve_value(self, keyword: str) -> object:
        if keyword.lower() == self.INTEREST:
            # Code to calculate the current variable interest rates.
            return 9.0

        if keyword.lower() == self.TARGET_DONE:
            # Code to check if the bank target of giving loans for the current year is done or not.
            return False

        return None

# # Example usage
# if __name__ == "__main__":
#     resolver = BankResolver()
#     print(resolver.get_resolver_keyword())  # Output: "bank"
#     print(resolver.resolve_value("interest"))  # Output: 9.0
#     print(resolver.resolve_value("target_done"))  # Output: False
#     print(resolver.resolve_value("unknown"))  # Output: None
