# CardNewResponse.CancelOpening - свойство
Признак того, что созданную карточку не следует открывать стандартными
средствами, как будто бы при её создании произошла ошибка. Это позволяет
заменить операцию на создание карточки операцией на выполнение действий с
созданной карточкой, например, по созданию карточки из загруженного шаблона.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool CancelOpening { get; set; }
VB __Копировать
     Public Property CancelOpening As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool CancelOpening {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member CancelOpening : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Значение по умолчанию false возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardNewResponse - ](T_Tessa_Cards_CardNewResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
