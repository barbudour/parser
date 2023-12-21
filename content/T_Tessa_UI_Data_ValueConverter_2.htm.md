# ValueConverter<TSource, TTarget> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ValueConverter<TSource, TTarget> : IValueConverter
VB __Копировать
     Public MustInherit Class ValueConverter(Of TSource, TTarget)
    	Implements IValueConverter
C++ __Копировать
    generic<typename TSource, typename TTarget>
    public ref class ValueConverter abstract : IValueConverter
F# __Копировать
     [<AbstractClassAttribute>]
    type ValueConverter<'TSource, 'TTarget> = 
        class
            interface IValueConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValueConverter<TSource, TTarget>
Derived
[Tessa.UI.Cards.Views.Blocks.BlockCaptionDockConverter](T_Tessa_UI_Cards_Views_Blocks_BlockCaptionDockConverter.htm)
[Tessa.UI.Cards.Views.Blocks.BlockCaptionMarginConverter](T_Tessa_UI_Cards_Views_Blocks_BlockCaptionMarginConverter.htm)
[Tessa.UI.Cards.Views.Blocks.BlockCaptionOrientationConverter](T_Tessa_UI_Cards_Views_Blocks_BlockCaptionOrientationConverter.htm)
[Tessa.UI.Cards.Views.CardDateTimeFormatConverter](T_Tessa_UI_Cards_Views_CardDateTimeFormatConverter.htm)
[Tessa.UI.Cards.Views.Editors.TabControlEditorSelectedItemConverter](T_Tessa_UI_Cards_Views_Editors_TabControlEditorSelectedItemConverter.htm)
[Tessa.UI.Cards.Views.Tasks.TaskHistoryDateTimeFormatConverter](T_Tessa_UI_Cards_Views_Tasks_TaskHistoryDateTimeFormatConverter.htm)
[Tessa.UI.Cards.Views.Tasks.TaskHistoryToolTipConverter](T_Tessa_UI_Cards_Views_Tasks_TaskHistoryToolTipConverter.htm)
[Tessa.UI.Controls.AutoCompleteCtrl.AutoCompleteToolTipConverter](T_Tessa_UI_Controls_AutoCompleteCtrl_AutoCompleteToolTipConverter.htm)
[Tessa.UI.Controls.Scrolling.ScrollingImageControlConverter](T_Tessa_UI_Controls_Scrolling_ScrollingImageControlConverter.htm)
[Tessa.UI.Controls.Scrolling.ScrollingItemPaddingConverter](T_Tessa_UI_Controls_Scrolling_ScrollingItemPaddingConverter.htm)
[Tessa.UI.Data.BooleanToDoubleConverter](T_Tessa_UI_Data_BooleanToDoubleConverter.htm)
[Tessa.UI.Data.BooleanToFlowDirectionConverter](T_Tessa_UI_Data_BooleanToFlowDirectionConverter.htm)
[Tessa.UI.Data.BooleanToHorizontalAlignmentConverter](T_Tessa_UI_Data_BooleanToHorizontalAlignmentConverter.htm)
[Tessa.UI.Data.BooleanToLeftRightHorizontalAlignmentConverter](T_Tessa_UI_Data_BooleanToLeftRightHorizontalAlignmentConverter.htm)
[Tessa.UI.Data.BooleanToScrollBarVisibilityConverter](T_Tessa_UI_Data_BooleanToScrollBarVisibilityConverter.htm)
[Tessa.UI.Data.BooleanToSelectionModeConverter](T_Tessa_UI_Data_BooleanToSelectionModeConverter.htm)
[Tessa.UI.Data.BooleanToVerticalAlignmentConverter](T_Tessa_UI_Data_BooleanToVerticalAlignmentConverter.htm)
[Tessa.UI.Data.BooleanToWrapingConverter](T_Tessa_UI_Data_BooleanToWrapingConverter.htm)
[Tessa.UI.Data.BrushOpacityConverter](T_Tessa_UI_Data_BrushOpacityConverter.htm)
[Tessa.UI.Data.ColorToSolidColorBrushConverter](T_Tessa_UI_Data_ColorToSolidColorBrushConverter.htm)
[Tessa.UI.Data.CountToVisibilityConverter](T_Tessa_UI_Data_CountToVisibilityConverter.htm)
[Tessa.UI.Data.CultureInfoToXmlLanguageConverter](T_Tessa_UI_Data_CultureInfoToXmlLanguageConverter.htm)
[Tessa.UI.Data.DoubleMultiplierConverter](T_Tessa_UI_Data_DoubleMultiplierConverter.htm)
[Tessa.UI.Data.EmptyValidationResultToNullConverter](T_Tessa_UI_Data_EmptyValidationResultToNullConverter.htm)
[Tessa.UI.Data.EmToLogicalUnitConverter](T_Tessa_UI_Data_EmToLogicalUnitConverter.htm)
[Tessa.UI.Data.FilePathToImageSourceConverter](T_Tessa_UI_Data_FilePathToImageSourceConverter.htm)
[Tessa.UI.Data.FormatDateConverter](T_Tessa_UI_Data_FormatDateConverter.htm)
[Tessa.UI.Data.IncrementDoubleConverter](T_Tessa_UI_Data_IncrementDoubleConverter.htm)
[Tessa.UI.Data.IndentToThicknessConverter](T_Tessa_UI_Data_IndentToThicknessConverter.htm)
[Tessa.UI.Data.IndexToNumberConverter](T_Tessa_UI_Data_IndexToNumberConverter.htm)
[Tessa.UI.Data.LocalizableFormatStringConverter](T_Tessa_UI_Data_LocalizableFormatStringConverter.htm)
[Tessa.UI.Data.LocalizableStringConverter](T_Tessa_UI_Data_LocalizableStringConverter.htm)
[Tessa.UI.Data.NegatedBooleanConverter](T_Tessa_UI_Data_NegatedBooleanConverter.htm)
[Tessa.UI.Data.NegatedBooleanToVisibilityConverter](T_Tessa_UI_Data_NegatedBooleanToVisibilityConverter.htm)
[Tessa.UI.Data.NegatedNullToBooleanConverter](T_Tessa_UI_Data_NegatedNullToBooleanConverter.htm)
[Tessa.UI.Data.NullToBooleanConverter](T_Tessa_UI_Data_NullToBooleanConverter.htm)
[Tessa.UI.Data.NullToCursorConverter](T_Tessa_UI_Data_NullToCursorConverter.htm)
[Tessa.UI.Data.NullToVisibilityConverter](T_Tessa_UI_Data_NullToVisibilityConverter.htm)
[Tessa.UI.Data.NumberToIndexConverter](T_Tessa_UI_Data_NumberToIndexConverter.htm)
[Tessa.UI.Data.ObjectOfTypeConverter](T_Tessa_UI_Data_ObjectOfTypeConverter.htm)
[Tessa.UI.Data.ObjectToCollectionViewConverter](T_Tessa_UI_Data_ObjectToCollectionViewConverter.htm)
[Tessa.UI.Data.ObjectToLocalizableStringConverter](T_Tessa_UI_Data_ObjectToLocalizableStringConverter.htm)
[Tessa.UI.Data.StorageToBrushConverter](T_Tessa_UI_Data_StorageToBrushConverter.htm)
[Tessa.UI.Data.StringLimitConverter](T_Tessa_UI_Data_StringLimitConverter.htm)
[Tessa.UI.Data.StringToFirstCharConverter](T_Tessa_UI_Data_StringToFirstCharConverter.htm)
[Tessa.UI.Data.StringTrimConverter](T_Tessa_UI_Data_StringTrimConverter.htm)
[Tessa.UI.Data.StringWidthLimitConverter](T_Tessa_UI_Data_StringWidthLimitConverter.htm)
[Tessa.UI.Data.ThicknessIncrementConverter](T_Tessa_UI_Data_ThicknessIncrementConverter.htm)
[Tessa.UI.Data.UIElementToVisibilityConverter](T_Tessa_UI_Data_UIElementToVisibilityConverter.htm)
[Tessa.UI.Data.UriToImageSourceConverter](T_Tessa_UI_Data_UriToImageSourceConverter.htm)
[Tessa.UI.Data.UtcToLocalDateTimeConverter](T_Tessa_UI_Data_UtcToLocalDateTimeConverter.htm)
[Tessa.UI.Files.Controls.Resources.DigitalSignaturesStateConverter](T_Tessa_UI_Files_Controls_Resources_DigitalSignaturesStateConverter.htm)
[Tessa.UI.Menu.MenuActionFontWeightConverter](T_Tessa_UI_Menu_MenuActionFontWeightConverter.htm)
[Tessa.UI.Scheme.ColumnsToPhysicalColumnsConverter](T_Tessa_UI_Scheme_ColumnsToPhysicalColumnsConverter.htm)
[Tessa.UI.Scheme.ColumnToDataGridColumnConverter](T_Tessa_UI_Scheme_ColumnToDataGridColumnConverter.htm)
[Tessa.UI.Scheme.Differences.SchemePropertyDifferenceToTextBlockConverter](T_Tessa_UI_Scheme_Differences_SchemePropertyDifferenceToTextBlockConverter.htm)
[Tessa.UI.Scheme.SortOrderToBooleanConverter](T_Tessa_UI_Scheme_SortOrderToBooleanConverter.htm)
[Tessa.UI.Views.Charting.Controls.ListToDoubleCollectionConverter](T_Tessa_UI_Views_Charting_Controls_ListToDoubleCollectionConverter.htm)
[Tessa.UI.Views.Charting.Legends.LegendLocationConverter](T_Tessa_UI_Views_Charting_Legends_LegendLocationConverter.htm)
[Tessa.UI.Views.Content.Table.ColumnCellTemplateConverter](T_Tessa_UI_Views_Content_Table_ColumnCellTemplateConverter.htm)
[Tessa.UI.Views.Content.Table.TableRowCollectionConverter](T_Tessa_UI_Views_Content_Table_TableRowCollectionConverter.htm)
[Tessa.UI.Views.Content.TableMultiSelectConverter](T_Tessa_UI_Views_Content_TableMultiSelectConverter.htm)
[Tessa.UI.Views.Filtering.FilteringToVisibilityConverter](T_Tessa_UI_Views_Filtering_FilteringToVisibilityConverter.htm)
[Tessa.UI.WorkflowViewer.Helpful.IsNodeExpandedToExpandButtonTextConverter](T_Tessa_UI_WorkflowViewer_Helpful_IsNodeExpandedToExpandButtonTextConverter.htm)
Подробнее __Less __
Implements
    [IValueConverter](https://learn.microsoft.com/dotnet/api/system.windows.data.ivalueconverter)
#### Параметры типа
TSource
TTarget
##  __Конструкторы
[ValueConverter<TSource,
TTarget>](M_Tessa_UI_Data_ValueConverter_2__ctor.htm)| Инициализирует новый
экземпляр класса ValueConverter<TSource, TTarget>  
---|---  
##  __Методы
[BoxSourceValue](M_Tessa_UI_Data_ValueConverter_2_BoxSourceValue.htm)|  
---|---  
[BoxTargetValue](M_Tessa_UI_Data_ValueConverter_2_BoxTargetValue.htm)|  
[Convert(TSource, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_Convert_1.htm)|  
[Convert(Object, Type, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_Convert.htm)|  
[ConvertBack(TTarget, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_ConvertBack_1.htm)|  
[ConvertBack(Object, Type, Object,
CultureInfo)](M_Tessa_UI_Data_ValueConverter_2_ConvertBack.htm)|  
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
