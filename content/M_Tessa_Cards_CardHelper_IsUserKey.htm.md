# CardHelper.IsUserKey - метод
Определяет, является ли заданный ключ хранилища IDictionary<string, object>
пользовательским ключом.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsUserKey(
    	string key
    )
VB __Копировать
     Public Shared Function IsUserKey ( 
    	key As String
    ) As Boolean
C++ __Копировать
     public:
    static bool IsUserKey(
    	String^ key
    )
F# __Копировать
     static member IsUserKey : 
            key : string -> bool 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, для которого требуется определить, является ли он пользовательским ключом.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный ключ является пользовательским ключом; false в противном
случае.
## __Заметки
Пользовательский ключ используется клиентскими или серверными расширениями, не
используется платформой, содержит произвольную информацию и удаляется при
передаче через границу клиент / сервер.
Пользовательские ключи рекомендуется использовать для хранения временной
информации, которую можно сохранять в произвольном месте карточки (или
похожего объекта
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)) и передавать
от одного клиентского или пользовательского расширения к другому.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
