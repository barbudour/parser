# CardRequest.CardID - свойство
Идентификатор карточки. Значение необязательно для заполнения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? CardID { get; set; }
VB __Копировать
     Public Property CardID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> CardID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member CardID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Значение по умолчанию null возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardRequest - ](T_Tessa_Cards_CardRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
