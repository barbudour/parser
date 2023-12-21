# ConditionHelper - класс
Вспомогательные свойства и методы для работы условий.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ConditionHelper
VB __Копировать
     Public NotInheritable Class ConditionHelper
C++ __Копировать
     public ref class ConditionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ConditionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConditionHelper
##  __Методы
[CleanConditionRowAsync](M_Tessa_Platform_Conditions_ConditionHelper_CleanConditionRowAsync.htm)|
Производит очистку строки условия от расширенных полей строковых секций,
содержащих настройки условия.  
---|---  
[DeserializeConditionRowAsync](M_Tessa_Platform_Conditions_ConditionHelper_DeserializeConditionRowAsync.htm)|
Выполняет десериализацию настроек условия в карточку.  
[DeserializeConditionsToEntrySectionAsync](M_Tessa_Platform_Conditions_ConditionHelper_DeserializeConditionsToEntrySectionAsync.htm)|
Десериализует секции с настройками условий из настроек, хранящихся в строковой
секции sectionName в поле fieldName переданной карточки.  
[GetConditionDescriptionAsync](M_Tessa_Platform_Conditions_ConditionHelper_GetConditionDescriptionAsync.htm)|
Выполняет генерацию описания условия.  
[GetExtendedFieldName](M_Tessa_Platform_Conditions_ConditionHelper_GetExtendedFieldName.htm)|
Возвращает расширенное имя поля для настроек условия по имени секции и имени
поля.  
[GetExtendedSectionName](M_Tessa_Platform_Conditions_ConditionHelper_GetExtendedSectionName.htm)|
Возвращает расширенное имя секции для настроек условия по имени секции.  
[GetOriginalSectionFieldName](M_Tessa_Platform_Conditions_ConditionHelper_GetOriginalSectionFieldName.htm)|
Возвращает оригинальные имена секции и поля по расширенному имени поля.  
[GetOriginalSectionName](M_Tessa_Platform_Conditions_ConditionHelper_GetOriginalSectionName.htm)|
Возвращает оригинальное имя секции по его расширенному имени.  
[IsConditionColumn](M_Tessa_Platform_Conditions_ConditionHelper_IsConditionColumn.htm)|
Определяет, используется ли поле для хранения настроек условия.  
[RowConditionToSettingsAsync](M_Tessa_Platform_Conditions_ConditionHelper_RowConditionToSettingsAsync.htm)|
Сериализует настройки условия в storage-объект.  
[SerializeConditionRowAsync](M_Tessa_Platform_Conditions_ConditionHelper_SerializeConditionRowAsync.htm)|
Сериализует настройки условия в JSON и сохраняет его в поле Settings строки
условия.  
[SerializeConditionSettingsAsync](M_Tessa_Platform_Conditions_ConditionHelper_SerializeConditionSettingsAsync.htm)|
Сериализует настройки условия в JSON.  
## __Поля
[ConditionExtensionPrefix](F_Tessa_Platform_Conditions_ConditionHelper_ConditionExtensionPrefix.htm)|
Префикс для определения принадлежности секции или поля к подсистеме условий.  
---|---  
[ConditionsBaseTypeID](F_Tessa_Platform_Conditions_ConditionHelper_ConditionsBaseTypeID.htm)|
Card type identifier for "ConditionsBase":
{0EB20600-F137-42AD-B007-440492200ACF}.  
[ConditionsBaseTypeName](F_Tessa_Platform_Conditions_ConditionHelper_ConditionsBaseTypeName.htm)|
Card type name for "ConditionsBase".  
[ConditionSectionName](F_Tessa_Platform_Conditions_ConditionHelper_ConditionSectionName.htm)|
Имя виртуальной секции с настройками условий.  
[ConditionTablesBlockName](F_Tessa_Platform_Conditions_ConditionHelper_ConditionTablesBlockName.htm)|
Имя блока, в который добавляется таблица с условиями.  
[EmptyConditionTypeID](F_Tessa_Platform_Conditions_ConditionHelper_EmptyConditionTypeID.htm)|
Card type identifier for "EmptyCondition":
{4B68414D-BF1A-4227-BB01-B1FC939D0E5A}.  
[EmptyConditionTypeName](F_Tessa_Platform_Conditions_ConditionHelper_EmptyConditionTypeName.htm)|
Card type name for "EmptyCondition".  
[TagKey](F_Tessa_Platform_Conditions_ConditionHelper_TagKey.htm)|  Имя ключа,
по которму в блоках и контролах формы с настройками условия записывается тип
условия, к которому относится элемент управления.  
## __См. также
#### Ссылки
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
