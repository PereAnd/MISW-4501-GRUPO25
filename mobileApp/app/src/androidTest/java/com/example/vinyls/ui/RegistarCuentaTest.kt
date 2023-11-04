package com.example.ingsoftappmobiles.ui


import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView.ViewHolder
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.action.ViewActions.closeSoftKeyboard
import androidx.test.espresso.action.ViewActions.typeText
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.contrib.RecyclerViewActions.actionOnItemAtPosition
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.filters.LargeTest
import com.example.vinyls.R
import com.example.vinyls.view.MainActivity
import org.hamcrest.Description
import org.hamcrest.Matcher
import org.hamcrest.Matchers.`is`
import org.hamcrest.Matchers.allOf
import org.hamcrest.TypeSafeMatcher
import org.hamcrest.core.IsInstanceOf
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@LargeTest
@RunWith(AndroidJUnit4::class)
class RegistarCuentaTest {

    @Rule
    @JvmField
    var mActivityScenarioRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun registroEInformacionAcademica() {
        /*val recyclerView = onView(
            allOf(
                withId(R.id.albumsRecyclerView),
                childAtPosition(
                    withClassName(`is`("androidx.constraintlayout.widget.ConstraintLayout")),
                    1
                )
            )
        )
        recyclerView.perform(actionOnItemAtPosition<ViewHolder>(3, click()))*/
        val loginButton = onView(allOf(withId(R.id.btnLogin)))
        loginButton.perform(click())

        val registerButton = onView(allOf(withId(R.id.buttonRegistro)))
        registerButton.perform(click())

        val namesText = onView(allOf(withId(R.id.etNamesRegistro)))
        namesText.check(matches(withHint("Nombres")))
        namesText.perform(typeText("Cesar"), closeSoftKeyboard())

        val lastNamesText = onView(allOf(withId(R.id.etLastNamesRegistro)))
        lastNamesText.check(matches(withHint("Apellidos")))
        lastNamesText.perform(typeText("Garcia"), closeSoftKeyboard())

        val mailText = onView(allOf(withId(R.id.etMailRegistro)))
        mailText.check(matches(withHint("E-Mail")))
        mailText.perform(typeText("cesa96@gmail.com"), closeSoftKeyboard())

        val passwordText = onView(allOf(withId(R.id.etPasswordRegistro)))
        passwordText.check(matches(withHint("Password")))
        passwordText.perform(typeText("123456789"), closeSoftKeyboard())

        val confirmText = onView(allOf(withId(R.id.etConfirmPasswordRegistro)))
        confirmText.check(matches(withHint("ConfirmPassword")))
        confirmText.perform(typeText("123456789"), closeSoftKeyboard())

        val saveButton = onView(allOf(withId(R.id.btnSendCandidato)))
        saveButton.perform(click())

        onView(allOf(withText("Datos enviados exitosamente."))).check(matches(isDisplayed()));

        val nextButton = onView(allOf(withId(R.id.btnNextAcademic)))
        nextButton.perform(click())

        val titleText = onView(allOf(withId(R.id.etTitle)))
        titleText.check(matches(withHint("Titulo obtenido")))
        titleText.perform(typeText("Ing. sistemas"), closeSoftKeyboard())

        val institutionText = onView(allOf(withId(R.id.etInstitution)))
        institutionText.check(matches(withHint("Institución")))
        institutionText.perform(typeText("UIS"), closeSoftKeyboard())

        val startText = onView(allOf(withId(R.id.etBeginDate)))
        startText.check(matches(withHint("Fecha de inicio")))
        startText.perform(typeText("2000-07-16T00:00:00.000Z"), closeSoftKeyboard())

        val endText = onView(allOf(withId(R.id.etEndDate)))
        endText.check(matches(withHint("Fecha de finalización")))
        endText.perform(typeText("2005-07-16T00:00:00.000Z"), closeSoftKeyboard())

        val typeText = onView(allOf(withId(R.id.etStudyType)))
        typeText.check(matches(withHint("Tipo de estudio")))
        typeText.perform(typeText("PREGRADO"), closeSoftKeyboard())

        val saveButtonInfo = onView(allOf(withId(R.id.btnSaveInfoAcademica)))
        saveButtonInfo.perform(click())

        onView(allOf(withText("Datos enviados exitosamente."))).check(matches(isDisplayed()));








        /*val appCompatImageButton = onView(
            allOf(
                withContentDescription("Navigate up"),
                childAtPosition(
                    allOf(
                        withId(androidx.constraintlayout.widget.R.id.action_bar),
                        childAtPosition(
                            withId(androidx.constraintlayout.widget.R.id.action_bar_container),
                            0
                        )
                    ),
                    2
                ),
                isDisplayed()
            )
        )
        appCompatImageButton.perform(click())

        val recyclerView2 = onView(
            allOf(
                withId(R.id.albumsRecyclerView),
                childAtPosition(
                    withClassName(`is`("androidx.constraintlayout.widget.ConstraintLayout")),
                    1
                )
            )
        )
        recyclerView2.perform(actionOnItemAtPosition<ViewHolder>(6, click()))

        val textView2 = onView(
            allOf(
                withId(R.id.text_release_date_label), withText("Lanzamiento:"),
                withParent(withParent(IsInstanceOf.instanceOf(android.widget.LinearLayout::class.java))),
                isDisplayed()
            )
        )
        textView2.check(matches(withText("Lanzamiento:")))

        val textView3 = onView(
            allOf(
                withId(R.id.text_tracks_title), withText("Canciones"),
                withParent(withParent(IsInstanceOf.instanceOf(android.widget.LinearLayout::class.java))),
                isDisplayed()
            )
        )
        textView3.check(matches(withText("Canciones")))

        val textView4 = onView(
            allOf(
                withId(R.id.text_comments_title), withText("Comentarios"),
                withParent(withParent(IsInstanceOf.instanceOf(android.widget.FrameLayout::class.java))),
                isDisplayed()
            )
        )
        textView4.check(matches(withText("Comentarios")))

        val textView5 = onView(
            allOf(
                withId(R.id.text_description_title), withText("Acerca del álbum"),
                withParent(withParent(IsInstanceOf.instanceOf(android.widget.FrameLayout::class.java))),
                isDisplayed()
            )
        )
        textView5.check(matches(withText("Acerca del álbum")))*/
    }

    private fun childAtPosition(
        parentMatcher: Matcher<View>, position: Int
    ): Matcher<View> {

        return object : TypeSafeMatcher<View>() {
            override fun describeTo(description: Description) {
                description.appendText("Child at position $position in parent ")
                parentMatcher.describeTo(description)
            }

            public override fun matchesSafely(view: View): Boolean {
                val parent = view.parent
                return parent is ViewGroup && parentMatcher.matches(parent)
                        && view == parent.getChildAt(position)
            }
        }
    }
}
