# CardMetadataBinder.RemoveRowAsync - метод
Выполняет удаление указанной строки из коллекционной или древовидной секции с
заданным именем, при этом учитывается возможное наличие строк в дочерних
секциях.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask RemoveRowAsync(
    	string sectionName,
    	CardRow row,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RemoveRowAsync ( 
    	sectionName As String,
    	row As CardRow,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask RemoveRowAsync(
    	String^ sectionName, 
    	CardRow^ row, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RemoveRowAsync : 
            sectionName : string * 
            row : CardRow * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override RemoveRowAsync : 
            sectionName : string * 
            row : CardRow * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, в которой содержится указанная строка.
row [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка, которую необходимо удалить из секции с заданным именем.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[ICardMetadataBinder.RemoveRowAsync(String, CardRow,
CancellationToken)](M_Tessa_Cards_Metadata_ICardMetadataBinder_RemoveRowAsync.htm)  
##  __Заметки
Строки физически удаляются из пакета только в том случае, если указанная
строка row была добавлена на клиенте, т.е. имеет состояние
[Inserted](T_Tessa_Cards_CardRowState.htm). Именно в этом случае удаляются
зависимые строки в дочерних секциях. В противном случае у строки row
устанавливается состояние [Deleted](T_Tessa_Cards_CardRowState.htm) и других
действий не производится.
## __См. также
#### Ссылки
[CardMetadataBinder - ](T_Tessa_Cards_Metadata_CardMetadataBinder.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
