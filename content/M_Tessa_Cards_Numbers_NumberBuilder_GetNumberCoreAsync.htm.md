# NumberBuilder.GetNumberCoreAsync - метод
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<INumberObject> GetNumberCoreAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	INumberLocation location,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function GetNumberCoreAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	location As INumberLocation,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     protected:
    virtual ValueTask<INumberObject^> GetNumberCoreAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	INumberLocation^ location, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetNumberCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            location : INumberLocation * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
    override GetNumberCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            location : INumberLocation * 
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
    Тип получаемого номера.
location [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
    Местоположение получаемого номера.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Номер, расположенный в заданных местоположении и контексте или пустой номер,
если он не был найден. Метод не возвращает null.
## __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
