# CardStoreRequest.ForceTransaction - свойство
Признак того, что для карточки будет принудительно открыта транзакция даже в
том случае, если изменения карточки отсутствуют. Это позволит гарантировать,
что расширения внутри транзакции будут выполнены. При отсутствии других
изменений в карточке транзакция будет открыта без блокировки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool ForceTransaction { get; set; }
VB __Копировать
     Public Property ForceTransaction As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool ForceTransaction {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member ForceTransaction : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Значение по умолчанию false возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
