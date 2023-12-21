# CardValidatorSettings - класс
Настройки стандартных валидаторов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardValidatorSettings
VB __Копировать
     Public NotInheritable Class CardValidatorSettings
C++ __Копировать
     public ref class CardValidatorSettings abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardValidatorSettings = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardValidatorSettings
##  __Поля
[ColumnIDSetting](F_Tessa_Cards_Validation_CardValidatorSettings_ColumnIDSetting.htm)|
Имя настройки, определяющей идентификатор колонки.  
---|---  
[ErrorMessageSetting](F_Tessa_Cards_Validation_CardValidatorSettings_ErrorMessageSetting.htm)|
Сообщение об ошибке или null или пустая строка, если используется стандартное
сообщение.  
[OrderColumnIDSetting](F_Tessa_Cards_Validation_CardValidatorSettings_OrderColumnIDSetting.htm)|
Имя настройки, определяющей идентификатор колонки для сортировки строк в
секции.  
[ParentColumnIDSetting](F_Tessa_Cards_Validation_CardValidatorSettings_ParentColumnIDSetting.htm)|
Имя настройки, определяющей идентификатор родительской колонки. Например,
такая колонка может ограничивать проверку уникальности только для значений в
пределах родительской колонки.  
[ParentSectionIDSetting](F_Tessa_Cards_Validation_CardValidatorSettings_ParentSectionIDSetting.htm)|
Имя настройки, определяющей идентификатор родительской секции. Обычно такая
секция содержит родительскую колонку
[ParentColumnIDSetting](F_Tessa_Cards_Validation_CardValidatorSettings_ParentColumnIDSetting.htm).  
[RemoveDuplicatesSetting](F_Tessa_Cards_Validation_CardValidatorSettings_RemoveDuplicatesSetting.htm)|
Признак того, что неуникальные значения (дубликаты) нужно автоматически
удалять.  
[SectionIDSetting](F_Tessa_Cards_Validation_CardValidatorSettings_SectionIDSetting.htm)|
Имя настройки, определяющей идентификатор секции.  
[WarningSetting](F_Tessa_Cards_Validation_CardValidatorSettings_WarningSetting.htm)|
Признак того, что вместо ошибки валидации пользователю выводится
предупреждение.  
## __См. также
#### Ссылки
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
