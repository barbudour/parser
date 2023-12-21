# NumberContext.ContextInfo - свойство
Доступная только для чтения информация из внешнего контекста, используемая при
обработке события, происходящего с номером. Обычно в расширениях UI это
ICardModel.Info, а в других расширениях, связанных с карточками, это Info
запроса.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject ContextInfo { get; }
VB __Копировать
     Public ReadOnly Property ContextInfo As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ ContextInfo {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract ContextInfo : ISerializableObject with get
    override ContextInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[INumberContext.ContextInfo](P_Tessa_Cards_Numbers_INumberContext_ContextInfo.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
