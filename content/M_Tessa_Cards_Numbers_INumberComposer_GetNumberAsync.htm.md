# INumberComposer.GetNumberAsync - метод
Возвращает номер заданного типа для контекста события, происходящего с
номером. Например, загружает номер из определённой позиции в карточке.
Возвращает пустой номер, если выполнить действие не удалось. Возвращённое
значение не может быть равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<INumberObject> GetNumberAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetNumberAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     ValueTask<INumberObject^> GetNumberAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetNumberAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Номер заданного типа для контекста действий с номером или пустой номер, если
действие не удалось выполнить.
## __См. также
#### Ссылки
[INumberComposer - ](T_Tessa_Cards_Numbers_INumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
