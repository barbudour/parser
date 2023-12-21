# NumberStorageObject.ToNumberObjectAsync - метод
Преобразует информацию по номеру, указанную в текущем объекте, в объект типа
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<INumberObject> ToNumberObjectAsync(
    	INumberBuilder builder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ToNumberObjectAsync ( 
    	builder As INumberBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     public:
    ValueTask<INumberObject^> ToNumberObjectAsync(
    	INumberBuilder^ builder, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member ToNumberObjectAsync : 
            builder : INumberBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
#### Параметры
builder [INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm)
     Объект, посредством которого создаётся объект [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm) со свойствами, полученными у текущего объекта. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Объект, реализующий интерфейс
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm) и информацию по
номеру, указанную в текущем объекте.
## __См. также
#### Ссылки
[NumberStorageObject - ](T_Tessa_Cards_Numbers_NumberStorageObject.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
