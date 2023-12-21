# CardStoreRequest.ForceReleaseLock - свойство
Признак того, что для карточки будет принудительно закрыта блокировка на
запись даже в том случае, если она не должна быть закрыта. Этот флаг имеет
смысл только в том случае, когда
[Method](P_Tessa_Cards_CardStoreRequest_Method.htm) равен
[Restore](T_Tessa_Cards_CardStoreMethod.htm). Актуально, например, при
восстановлении карточки-сателлита.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool ForceReleaseLock { get; set; }
VB __Копировать
     Public Property ForceReleaseLock As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool ForceReleaseLock {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member ForceReleaseLock : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Значение по умолчанию false возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
