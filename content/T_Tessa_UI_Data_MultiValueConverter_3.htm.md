# MultiValueConverter<TSource1, TSource2, TTarget> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class MultiValueConverter<TSource1, TSource2, TTarget> : IMultiValueConverter
VB __Копировать
     Public MustInherit Class MultiValueConverter(Of TSource1, TSource2, TTarget)
    	Implements IMultiValueConverter
C++ __Копировать
    generic<typename TSource1, typename TSource2, typename TTarget>
    public ref class MultiValueConverter abstract : IMultiValueConverter
F# __Копировать
     [<AbstractClassAttribute>]
    type MultiValueConverter<'TSource1, 'TSource2, 'TTarget> = 
        class
            interface IMultiValueConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MultiValueConverter<TSource1, TSource2, TTarget>
Derived
[Tessa.UI.Cards.Blocks.RequiredControlCaptionConverter](T_Tessa_UI_Cards_Blocks_RequiredControlCaptionConverter.htm)
[Tessa.UI.Cards.Views.Controls.AvalonLinesToHeightConverter](T_Tessa_UI_Cards_Views_Controls_AvalonLinesToHeightConverter.htm)
[Tessa.UI.Cards.Views.Controls.DateTimeFormatToMinWidthConverter](T_Tessa_UI_Cards_Views_Controls_DateTimeFormatToMinWidthConverter.htm)
[Tessa.UI.Cards.Views.Tasks.TaskBackgroundConverter](T_Tessa_UI_Cards_Views_Tasks_TaskBackgroundConverter.htm)
[Tessa.UI.Cards.Views.Tasks.TaskBackgroundOpacityConverter](T_Tessa_UI_Cards_Views_Tasks_TaskBackgroundOpacityConverter.htm)
[Tessa.UI.Controls.Scrolling.ScrollingPreviewBorderBrushConverter](T_Tessa_UI_Controls_Scrolling_ScrollingPreviewBorderBrushConverter.htm)
[Tessa.UI.Controls.TopThicknessMultiValueConverter](T_Tessa_UI_Controls_TopThicknessMultiValueConverter.htm)
[Tessa.UI.Data.BooleanWithVisibilityConverter](T_Tessa_UI_Data_BooleanWithVisibilityConverter.htm)
[Tessa.UI.Data.ColorCoalesceConverter](T_Tessa_UI_Data_ColorCoalesceConverter.htm)
[Tessa.UI.Data.ColorToSolidColorBrushCoalesceConverter](T_Tessa_UI_Data_ColorToSolidColorBrushCoalesceConverter.htm)
[Tessa.UI.Data.DoubleMultiplierMultiConverter](T_Tessa_UI_Data_DoubleMultiplierMultiConverter.htm)
[Tessa.UI.Data.ReferenceEqualityValueConverter](T_Tessa_UI_Data_ReferenceEqualityValueConverter.htm)
[Tessa.UI.Data.StrokeDashProportionConverter](T_Tessa_UI_Data_StrokeDashProportionConverter.htm)
[Tessa.UI.Scheme.ColumnToReferencingColumnExistanceConverter](T_Tessa_UI_Scheme_ColumnToReferencingColumnExistanceConverter.htm)
Подробнее __Less __
Implements
    [IMultiValueConverter](https://learn.microsoft.com/dotnet/api/system.windows.data.imultivalueconverter)
#### Параметры типа
TSource1
TSource2
TTarget
##  __Конструкторы
[MultiValueConverter<TSource1, TSource2,
TTarget>](M_Tessa_UI_Data_MultiValueConverter_3__ctor.htm)| Инициализирует
новый экземпляр класса MultiValueConverter<TSource1, TSource2, TTarget>  
---|---  
##  __Методы
[BoxSourceValue1](M_Tessa_UI_Data_MultiValueConverter_3_BoxSourceValue1.htm)|  
---|---  
[BoxSourceValue2](M_Tessa_UI_Data_MultiValueConverter_3_BoxSourceValue2.htm)|  
[BoxTargetValue](M_Tessa_UI_Data_MultiValueConverter_3_BoxTargetValue.htm)|  
[Convert(TSource1, TSource2, Object,
CultureInfo)](M_Tessa_UI_Data_MultiValueConverter_3_Convert_1.htm)|  
[Convert(Object[], Type, Object,
CultureInfo)](M_Tessa_UI_Data_MultiValueConverter_3_Convert.htm)|  
[ConvertBack(Object, Type[], Object,
CultureInfo)](M_Tessa_UI_Data_MultiValueConverter_3_ConvertBack.htm)|  
[ConvertBack(TTarget, TSource1, TSource2, Object,
CultureInfo)](M_Tessa_UI_Data_MultiValueConverter_3_ConvertBack_1.htm)|  
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
