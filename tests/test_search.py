import pytest

from pages.home_page import UnitedUs


class TestSimpleFilterByName:

    @pytest.mark.nondestructive
    def test_filter_providers_by_need(self, base_url, selenium):
        '''
            For the following acceptance criteria of the Public Resource
            Directory: Given I have loaded all providers in North Carolina
            When I filter providers by need
            Then I should see providers filtered by my selected need

            Verify you can filter providers by need in a browser-based,
            user-interface test: Write a test case with one assertion
            you would make.
        '''
        pass

    @pytest.mark.nondestructive
    def test_search(self, base_url, selenium):
        '''
        Excercise #2
        '''
        home_page = UnitedUs(selenium, base_url).open()
        home_page.filters.search_by_name('service')

        # click first result to open the detailed view
        first_result = home_page.results[0].click_result()
        assert home_page.is_results_drawer_open

        # verify results info for the first item matches the detailed view's info
        assert first_result.name == home_page.detailed_results.name
        assert first_result.provider_name == home_page.detailed_results.provider_name
        assert first_result.address == home_page.detailed_results.address
        assert first_result.services == home_page.detailed_results.services
