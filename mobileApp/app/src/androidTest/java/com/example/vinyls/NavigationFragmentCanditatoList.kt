package com.example.vinyls

import androidx.fragment.app.testing.FragmentScenario
import androidx.fragment.app.testing.launchFragmentInContainer
import androidx.navigation.Navigation
import androidx.navigation.testing.TestNavHostController
import androidx.test.core.app.ApplicationProvider
import androidx.test.espresso.Espresso
import androidx.test.espresso.assertion.ViewAssertions
import androidx.test.espresso.matcher.ViewMatchers
import androidx.test.ext.junit.runners.AndroidJUnit4
import com.example.vinyls.R
import com.example.vinyls.view.FragmentCandidatoList
import org.hamcrest.Matchers
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class NavigationFragmentCanditatoList {
    lateinit var navController: TestNavHostController
    lateinit var homeMenuScenario : FragmentScenario<FragmentCandidatoList>

    @Before
    fun setup(){
        navController = TestNavHostController(
            ApplicationProvider.getApplicationContext()
        )
        homeMenuScenario = launchFragmentInContainer(
            themeResId = R.style.Theme_Vinyls
        )
        homeMenuScenario.onFragment{ fragment ->
            navController.setGraph(R.navigation.nav_graph)

            Navigation.setViewNavController(fragment.requireView(), navController)

        }
    }

    @Test
    fun check_textview_top(){
        Espresso.onView(ViewMatchers.withId(R.id.textViewCandidatos))
            .check(ViewAssertions.matches(ViewMatchers.withText(Matchers.containsString("Candidatos"))))

    }
}