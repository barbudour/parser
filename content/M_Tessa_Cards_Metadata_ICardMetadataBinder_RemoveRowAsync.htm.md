# ICardMetadataBinder.RemoveRowAsync - метод
Выполняет удаление указанной строки из коллекционной или древовидной секции с
заданным именем, при этом учитывается возможное наличие строк в дочерних
секциях.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask RemoveRowAsync(
    	string sectionName,
    	CardRow row,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function RemoveRowAsync ( 
    	sectionName As String,
    	row As CardRow,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask RemoveRowAsync(
    	String^ sectionName, 
    	CardRow^ row, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract RemoveRowAsync : 
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
##  __См. также
#### Ссылки
[ICardMetadataBinder - ](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
