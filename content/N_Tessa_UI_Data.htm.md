# Tessa.UI.Data - пространство имён
Вспомогательные классы для организации UI по редактированию данных.
##  __Классы
[BooleanLogicalAndConverter](T_Tessa_UI_Data_BooleanLogicalAndConverter.htm)|
Конвертер для выстраивания цепочки конвертеров. Выполняет операцию логического
И.  
---|---  
[BooleanLogicalOrConverter](T_Tessa_UI_Data_BooleanLogicalOrConverter.htm)|
Конвертер для выстраивания цепочки конвертеров. Выполняет операцию логического
ИЛИ.  
[BooleanToDoubleConverter](T_Tessa_UI_Data_BooleanToDoubleConverter.htm)|  
[BooleanToFlowDirectionConverter](T_Tessa_UI_Data_BooleanToFlowDirectionConverter.htm)|  
[BooleanToHorizontalAlignmentConverter](T_Tessa_UI_Data_BooleanToHorizontalAlignmentConverter.htm)|  
[BooleanToLeftRightHorizontalAlignmentConverter](T_Tessa_UI_Data_BooleanToLeftRightHorizontalAlignmentConverter.htm)|  
[BooleanToScrollBarVisibilityConverter](T_Tessa_UI_Data_BooleanToScrollBarVisibilityConverter.htm)|
Конвертер преобразует логическое значение, получаемое на входе привязки, к
значению перечисления
[ScrollBarVisibility](https://learn.microsoft.com/dotnet/api/system.windows.controls.scrollbarvisibility),
где true соответствует значению
[Auto](https://learn.microsoft.com/dotnet/api/system.windows.controls.scrollbarvisibility),
а false \- значению
[Disabled](https://learn.microsoft.com/dotnet/api/system.windows.controls.scrollbarvisibility).  
[BooleanToSelectionModeConverter](T_Tessa_UI_Data_BooleanToSelectionModeConverter.htm)|  
[BooleanToVerticalAlignmentConverter](T_Tessa_UI_Data_BooleanToVerticalAlignmentConverter.htm)|  
[BooleanToWrapingConverter](T_Tessa_UI_Data_BooleanToWrapingConverter.htm)|  
[BooleanWithVisibilityConverter](T_Tessa_UI_Data_BooleanWithVisibilityConverter.htm)|
Возвращает
[Visible](https://learn.microsoft.com/dotnet/api/system.windows.visibility)
если передан true, иначе возвращает второй параметр  
[BrushOpacityConverter](T_Tessa_UI_Data_BrushOpacityConverter.htm)|
Возвращает кисть с указанной непрозрачностью
[Opacity](P_Tessa_UI_Data_BrushOpacityConverter_Opacity.htm). Поддерживает
типы данных:
[Color](https://learn.microsoft.com/dotnet/api/system.windows.media.color),
[Brush](https://learn.microsoft.com/dotnet/api/system.windows.media.brush),
[StorageColor](T_Tessa_Platform_Storage_StorageColor.htm),
[StorageLinearGradientBrush](T_Tessa_Platform_Storage_StorageLinearGradientBrush.htm).  
[CollectionViewSourceHelper](T_Tessa_UI_Data_CollectionViewSourceHelper.htm)|  
[ColorCoalesceConverter](T_Tessa_UI_Data_ColorCoalesceConverter.htm)|  
[ColorToSolidColorBrushCoalesceConverter](T_Tessa_UI_Data_ColorToSolidColorBrushCoalesceConverter.htm)|  
[ColorToSolidColorBrushConverter](T_Tessa_UI_Data_ColorToSolidColorBrushConverter.htm)|  
[ColorToSolidColorBrushWithInversionOnMouseOverConverter](T_Tessa_UI_Data_ColorToSolidColorBrushWithInversionOnMouseOverConverter.htm)|  
[ComboBoxTemplateSelector](T_Tessa_UI_Data_ComboBoxTemplateSelector.htm)|  
[ConditionalValueConverter](T_Tessa_UI_Data_ConditionalValueConverter.htm)|  
[CopyableColumnViewModelCollection](T_Tessa_UI_Data_CopyableColumnViewModelCollection.htm)|  
[CountToVisibilityConverter](T_Tessa_UI_Data_CountToVisibilityConverter.htm)|  
[CultureInfoToXmlLanguageConverter](T_Tessa_UI_Data_CultureInfoToXmlLanguageConverter.htm)|  
[DataResource](T_Tessa_UI_Data_DataResource.htm)|  
[DataResourceBindingExtension](T_Tessa_UI_Data_DataResourceBindingExtension.htm)|  
[DoubleMultiplierConverter](T_Tessa_UI_Data_DoubleMultiplierConverter.htm)|
Конвертер умножает два числа, одно из которых получается на входе привязки, а
второе - в параметре конвертера.  
[DoubleMultiplierMultiConverter](T_Tessa_UI_Data_DoubleMultiplierMultiConverter.htm)|
Конвертер умножает два числа, получаемые на входе привязки.  
[EmptyValidationResultToNullConverter](T_Tessa_UI_Data_EmptyValidationResultToNullConverter.htm)|  
[EmToLogicalUnitConverter](T_Tessa_UI_Data_EmToLogicalUnitConverter.htm)|  
[EnumToStringConverter](T_Tessa_UI_Data_EnumToStringConverter.htm)|  
[FilePathToImageSourceConverter](T_Tessa_UI_Data_FilePathToImageSourceConverter.htm)|
Преобразует строку с Uri к файлу с изображением в объект-наследник
[ImageSource](https://learn.microsoft.com/dotnet/api/system.windows.media.imagesource).
Рекомендуется использовать такой конвертер, когда нужно, чтобы контрол,
выводящий изображение, не блокировал бы файл.  
[FormatDateConverter](T_Tessa_UI_Data_FormatDateConverter.htm)|  Конвертер,
преобразующий дату в строку по методу [FormatDate(Nullable<DateTime>,
Boolean)](M_Tessa_Platform_FormattingHelper_FormatDate_1.htm).  
[GroupView](T_Tessa_UI_Data_GroupView.htm)|  
[GroupViewCollection](T_Tessa_UI_Data_GroupViewCollection.htm)|  
[IfElseValueConverter](T_Tessa_UI_Data_IfElseValueConverter.htm)|  
[IncrementDoubleConverter](T_Tessa_UI_Data_IncrementDoubleConverter.htm)|  
[IndentToThicknessConverter](T_Tessa_UI_Data_IndentToThicknessConverter.htm)|  
[IndexToNumberConverter](T_Tessa_UI_Data_IndexToNumberConverter.htm)|  
[LocalizableFormatStringConverter](T_Tessa_UI_Data_LocalizableFormatStringConverter.htm)|  
[LocalizableStringConverter](T_Tessa_UI_Data_LocalizableStringConverter.htm)|  
[MultiValueConverter<TSource1, TSource2,
TTarget>](T_Tessa_UI_Data_MultiValueConverter_3.htm)|  
[MultiValueConverter<TSource1, TSource2, TSource3,
TTarget>](T_Tessa_UI_Data_MultiValueConverter_4.htm)|  
[MultiValueConverter<TSource1, TSource2, TSource3, TSource4,
TTarget>](T_Tessa_UI_Data_MultiValueConverter_5.htm)|  
[MultiValueConverter<TSource1, TSource2, TSource3, TSource4, TSource5,
TTarget>](T_Tessa_UI_Data_MultiValueConverter_6.htm)|  
[NegatedBooleanConverter](T_Tessa_UI_Data_NegatedBooleanConverter.htm)|  
[NegatedBooleanToVisibilityConverter](T_Tessa_UI_Data_NegatedBooleanToVisibilityConverter.htm)|  
[NegatedNullToBooleanConverter](T_Tessa_UI_Data_NegatedNullToBooleanConverter.htm)|  
[NullToBooleanConverter](T_Tessa_UI_Data_NullToBooleanConverter.htm)|  
[NullToCursorConverter](T_Tessa_UI_Data_NullToCursorConverter.htm)|  
[NullToGivenStringConverter](T_Tessa_UI_Data_NullToGivenStringConverter.htm)|
Заменяет null значения заданной строкой.  
[NullToParameterConverter](T_Tessa_UI_Data_NullToParameterConverter.htm)|  
[NullToVisibilityConverter](T_Tessa_UI_Data_NullToVisibilityConverter.htm)|
The null to visibility converter.  
[NumberToIndexConverter](T_Tessa_UI_Data_NumberToIndexConverter.htm)|  
[ObjectForContainerExtension](T_Tessa_UI_Data_ObjectForContainerExtension.htm)|  
[ObjectOfTypeConverter](T_Tessa_UI_Data_ObjectOfTypeConverter.htm)|  
[ObjectTemplate](T_Tessa_UI_Data_ObjectTemplate.htm)|  
[ObjectTemplateContent](T_Tessa_UI_Data_ObjectTemplateContent.htm)|  
[ObjectTemplateLoader](T_Tessa_UI_Data_ObjectTemplateLoader.htm)|  
[ObjectToCollectionViewConverter](T_Tessa_UI_Data_ObjectToCollectionViewConverter.htm)|  
[ObjectToContainerConverter](T_Tessa_UI_Data_ObjectToContainerConverter.htm)|  
[ObjectToLocalizableStringConverter](T_Tessa_UI_Data_ObjectToLocalizableStringConverter.htm)|  
[PropertyPathHelper](T_Tessa_UI_Data_PropertyPathHelper.htm)|  
[ReferenceEqualityValueConverter](T_Tessa_UI_Data_ReferenceEqualityValueConverter.htm)|
Сравнивает два значения на ссылочное равенство.  
[StorageToBrushConverter](T_Tessa_UI_Data_StorageToBrushConverter.htm)|
Преобразует значения [StorageColor](T_Tessa_Platform_Storage_StorageColor.htm)
или
[StorageLinearGradientBrush](T_Tessa_Platform_Storage_StorageLinearGradientBrush.htm)
в соответствующую кисть
[SolidColorBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.solidcolorbrush)
или
[LinearGradientBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.lineargradientbrush).  
[StorageToWpfConverter](T_Tessa_UI_Data_StorageToWpfConverter.htm)|
Преобразует значения в типы, совместимые с WPF:
[StorageColor](T_Tessa_Platform_Storage_StorageColor.htm) в
[Color](https://learn.microsoft.com/dotnet/api/system.windows.media.color),
[StorageLinearGradientBrush](T_Tessa_Platform_Storage_StorageLinearGradientBrush.htm)
в
[LinearGradientBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.lineargradientbrush).  
[StringLimitConverter](T_Tessa_UI_Data_StringLimitConverter.htm)|  
[StringToFirstCharConverter](T_Tessa_UI_Data_StringToFirstCharConverter.htm)|  
[StringTrimConverter](T_Tessa_UI_Data_StringTrimConverter.htm)|  
[StringWidthLimitConverter](T_Tessa_UI_Data_StringWidthLimitConverter.htm)|  
[StrokeDashProportionConverter](T_Tessa_UI_Data_StrokeDashProportionConverter.htm)|  
[SwitchCase](T_Tessa_UI_Data_SwitchCase.htm)|  
[SwitchCaseCollection](T_Tessa_UI_Data_SwitchCaseCollection.htm)|  
[SwitchCaseValueConverter](T_Tessa_UI_Data_SwitchCaseValueConverter.htm)|  
[ThicknessIncrementConverter](T_Tessa_UI_Data_ThicknessIncrementConverter.htm)|  
[TileAreaWidthConverter](T_Tessa_UI_Data_TileAreaWidthConverter.htm)|
Конвертер, преобразующий высоту боковой панели в ширину области с верхнего и
нижнего краёв экрана, по которой можно открыть боковую панель.  
[TreeCollectionView](T_Tessa_UI_Data_TreeCollectionView.htm)|  
[TreeCollectionViewGroup](T_Tessa_UI_Data_TreeCollectionViewGroup.htm)|  
[TreeGroupDescription](T_Tessa_UI_Data_TreeGroupDescription.htm)|  
[TreeLeafGroupDescription](T_Tessa_UI_Data_TreeLeafGroupDescription.htm)|  
[TreePropertyGroupDescription](T_Tessa_UI_Data_TreePropertyGroupDescription.htm)|  
[UIElementToVisibilityConverter](T_Tessa_UI_Data_UIElementToVisibilityConverter.htm)|  
[UriToImageSourceConverter](T_Tessa_UI_Data_UriToImageSourceConverter.htm)|
Преобразует [Uri](https://learn.microsoft.com/dotnet/api/system.uri) в
[ImageSource](https://learn.microsoft.com/dotnet/api/system.windows.media.imagesource),
использующий ссылку на ресурс в качестве изображения
[BitmapImage](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapimage)/
Параметр конвертера может использоваться в качестве значения по умолчанию.  
[UtcToLocalDateTimeConverter](T_Tessa_UI_Data_UtcToLocalDateTimeConverter.htm)|  
[ValueConverter<TSource, TTarget>](T_Tessa_UI_Data_ValueConverter_2.htm)|  
## __Интерфейсы
[IObjectForContainerProvider](T_Tessa_UI_Data_IObjectForContainerProvider.htm)|  
---|---
