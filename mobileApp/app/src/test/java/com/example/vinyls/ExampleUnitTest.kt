package com.example.vinyls
import org.junit.Test
import org.junit.Assert.*

import androidx.fragment.app.testing.FragmentScenario
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Before
import org.junit.runner.RunWith
import org.junit.Assert.*
import com.example.vinyls.view.FragmentRegistro
import kotlinx.android.synthetic.main.fragment_registro.*
import java.util.*


@RunWith(AndroidJUnit4::class)
class FragmentRegistroTest {

    private lateinit var fragmentScenario: FragmentScenario<FragmentRegistro>

    @Before
    fun setup() {
        // Inicializa el escenario del fragmento
        fragmentScenario = FragmentScenario.launchInContainer(FragmentRegistro::class.java)
    }

    @Test
    fun validateForm_WhenFieldsAreEmpty_ReturnsFalse() {
        // Arrange: No ingresamos datos en los campos

        // Act
        val result = fragmentScenario.onFragment { fragment ->
            // Llamamos a la función validateForm() del fragmento
            fragment.validateForm()
        }

        // Assert: Debería retornar falso
        assertFalse(result)
    }

    @Test
    fun validateForm_WhenFieldsAreNotEmpty_ReturnsTrue() {
        // Arrange: Ingresamos datos válidos en los campos

        // Act
        val result = fragmentScenario.onFragment { fragment ->
            // Llamamos a la función validateForm() del fragmento
            fragment.validateForm()
        }

        // Assert: Debería retornar verdadero
        assertTrue(result)
    }
}
