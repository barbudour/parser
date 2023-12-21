# IfElseValueConverter - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
    [XamlSetMarkupExtensionAttribute("ReceiveMarkupExtension")]
    [XamlSetTypeConverterAttribute("ReceiveTypeConverter")]
    public sealed class IfElseValueConverter : ConditionalValueConverter
VB __Копировать
    <XamlSetMarkupExtensionAttribute("ReceiveMarkupExtension")>
    <XamlSetTypeConverterAttribute("ReceiveTypeConverter")>
    Public NotInheritable Class IfElseValueConverter
    	Inherits ConditionalValueConverter
C++ __Копировать
    [XamlSetMarkupExtensionAttribute(L"ReceiveMarkupExtension")]
    [XamlSetTypeConverterAttribute(L"ReceiveTypeConverter")]
    public ref class IfElseValueConverter sealed : public ConditionalValueConverter
F# __Копировать
     [<SealedAttribute>]
    [<XamlSetMarkupExtensionAttribute("ReceiveMarkupExtension")>]
    [<XamlSetTypeConverterAttribute("ReceiveTypeConverter")>]
    type IfElseValueConverter = 
        class
            inherit ConditionalValueConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm) __ IfElseValueConverter
##  __Конструкторы
[IfElseValueConverter()](M_Tessa_UI_Data_IfElseValueConverter__ctor.htm)|
Инициализирует новый экземпляр класса IfElseValueConverter  
---|---  
[IfElseValueConverter(IEqualityComparer)](M_Tessa_UI_Data_IfElseValueConverter__ctor_1.htm)|
Инициализирует новый экземпляр класса IfElseValueConverter  
##  __Свойства
[Comparer](P_Tessa_UI_Data_IfElseValueConverter_Comparer.htm)|  
---|---  
[IfFalseValue](P_Tessa_UI_Data_IfElseValueConverter_IfFalseValue.htm)|  
[IfTrueValue](P_Tessa_UI_Data_IfElseValueConverter_IfTrueValue.htm)|  
[ReturnValueType](P_Tessa_UI_Data_ConditionalValueConverter_ReturnValueType.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
[TestValue](P_Tessa_UI_Data_IfElseValueConverter_TestValue.htm)|  
[TestValueType](P_Tessa_UI_Data_ConditionalValueConverter_TestValueType.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
##  __Методы
[BeginInit](M_Tessa_UI_Data_ConditionalValueConverter_BeginInit.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
---|---  
[BeginInitOverride](M_Tessa_UI_Data_ConditionalValueConverter_BeginInitOverride.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
[CheckInitializationPending](M_Tessa_UI_Data_ConditionalValueConverter_CheckInitializationPending.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
[CheckIsInitialized](M_Tessa_UI_Data_ConditionalValueConverter_CheckIsInitialized.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
[Convert(Object, Object,
CultureInfo)](M_Tessa_UI_Data_IfElseValueConverter_Convert.htm)|  
(Переопределяет [ConditionalValueConverter.Convert(Object, Object,
CultureInfo)](M_Tessa_UI_Data_ConditionalValueConverter_Convert.htm))  
[Convert(Object, Type, Object,
CultureInfo)](M_Tessa_UI_Data_ConditionalValueConverter_Convert_1.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
[ConvertBack(Object, Object,
CultureInfo)](M_Tessa_UI_Data_IfElseValueConverter_ConvertBack.htm)|  
(Переопределяет [ConditionalValueConverter.ConvertBack(Object, Object,
CultureInfo)](M_Tessa_UI_Data_ConditionalValueConverter_ConvertBack.htm))  
[ConvertBack(Object, Type, Object,
CultureInfo)](M_Tessa_UI_Data_ConditionalValueConverter_ConvertBack_1.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
[EndInit](M_Tessa_UI_Data_ConditionalValueConverter_EndInit.htm)|  
(Унаследован от
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm))  
[EndInitOverride](M_Tessa_UI_Data_IfElseValueConverter_EndInitOverride.htm)|  
(Переопределяет
[ConditionalValueConverter.EndInitOverride()](M_Tessa_UI_Data_ConditionalValueConverter_EndInitOverride.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ReceiveMarkupExtension](M_Tessa_UI_Data_IfElseValueConverter_ReceiveMarkupExtension.htm)|  
[ReceiveTypeConverter](M_Tessa_UI_Data_IfElseValueConverter_ReceiveTypeConverter.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.UI.Data - пространство имён](N_Tessa_UI_Data.htm)
