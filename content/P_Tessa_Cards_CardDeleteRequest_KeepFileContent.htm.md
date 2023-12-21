# CardDeleteRequest.KeepFileContent - свойство
Признак того, что контент файлов не должен быть удалён при удалении карточки.
Значение следует устанавливать только при вызове серверного API. При этом
информацию по наличию файлов будет удалена, поэтому указывайте значение true
только в том случае, если вызывающий код самостоятельно будет заботиться об
удалении контента.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool KeepFileContent { get; set; }
VB __Копировать
     Public Property KeepFileContent As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool KeepFileContent {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member KeepFileContent : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Значение по умолчанию false возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardDeleteRequest - ](T_Tessa_Cards_CardDeleteRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
