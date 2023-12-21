# INumberContext.ContextInfo - свойство
Доступная только для чтения информация из внешнего контекста, используемая при
обработке события, происходящего с номером. Обычно в расширениях UI это
ICardModel.Info, а в других расширениях, связанных с карточками, это Info
запроса.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ISerializableObject ContextInfo { get; }
VB __Копировать
     ReadOnly Property ContextInfo As ISerializableObject
    	Get
C++ __Копировать
    property ISerializableObject^ ContextInfo {
    	ISerializableObject^ get ();
    }
F# __Копировать
     abstract ContextInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[INumberContext - ](T_Tessa_Cards_Numbers_INumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
