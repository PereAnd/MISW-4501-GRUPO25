package com.example.vinyls.view

import android.os.SystemClock
import androidx.recyclerview.widget.RecyclerView
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.contrib.RecyclerViewActions
import androidx.test.espresso.contrib.RecyclerViewActions.actionOnItemAtPosition
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import com.example.vinyls.R
import org.hamcrest.Matchers.containsString
import org.junit.Assert.*
import org.junit.Before
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith


@RunWith(AndroidJUnit4::class)
class MainActivityTest {
    @get:Rule
    var mActivityTestRule = ActivityScenarioRule(MainActivity::class.java)

    @Before
    fun setUp() {}

    @Test
    fun homeIconNavigateToMainPage() {

        onView(withId(R.id.mainActivity)).check(matches(isDisplayed()))
    }

    @Test
    fun validateHomeText() {
        onView(withId(R.id.btnLogin)).check(matches(withText(containsString("Ingreso candidato"))))
    }

    @Test
    fun navigateToLogin() {
        onView(withId(R.id.buttonRegistro)).perform(click())
        onView(withId(R.id.buttonEntrevista)).check(matches(isDisplayed()))
    }


}