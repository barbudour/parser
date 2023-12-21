# CardNewRequest.CardTypeID - свойство
Идентификатор типа создаваемой карточки или null, если карточка создаётся по
виртуальному типу. Значение необязательно для заполнения, т.к. может быть
заполнено только свойство
[CardTypeName](P_Tessa_Cards_CardNewRequest_CardTypeName.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? CardTypeID { get; set; }
VB __Копировать
     Public Property CardTypeID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> CardTypeID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member CardTypeID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Значение по умолчанию null возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardNewRequest - ](T_Tessa_Cards_CardNewRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
