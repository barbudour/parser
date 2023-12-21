# ICardValidationContext.ExternalContextInfo - свойство
Произвольно структурированная информация из внешнего контекста (например,
контекста сохранения карточки), которая может быть заполнена валидатором и
использована либо другими валидаторами, либо внешними расширениями. Когда
внешний контекст неизвестен, будет создан пустой объект, но при этом свойство
никогда не возвращает null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ISerializableObject ExternalContextInfo { get; }
VB __Копировать
     ReadOnly Property ExternalContextInfo As ISerializableObject
    	Get
C++ __Копировать
    property ISerializableObject^ ExternalContextInfo {
    	ISerializableObject^ get ();
    }
F# __Копировать
     abstract ExternalContextInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __См. также
#### Ссылки
[ICardValidationContext -
](T_Tessa_Cards_Validation_ICardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
