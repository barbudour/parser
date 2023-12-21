# CardStoreResponse.StoreDateTime - свойство
Дата сохранения карточки (которая записана как дата изменения карточки), или
null, если карточка не была изменена, сохранение не было выполнено успешно или
сохранена виртуальная карточка, для которой это свойство не заполнено.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DateTime? StoreDateTime { get; set; }
VB __Копировать
     Public Property StoreDateTime As DateTime?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<DateTime> StoreDateTime {
    	Nullable<DateTime> get ();
    	void set (Nullable<DateTime> value);
    }
F# __Копировать
     member StoreDateTime : Nullable<DateTime> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
##  __Заметки
Свойство заполняется платформой.
##  __См. также
#### Ссылки
[CardStoreResponse - ](T_Tessa_Cards_CardStoreResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
