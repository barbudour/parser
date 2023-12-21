# NumberBuilder.TryGetNumberLocationAsync - метод
Возвращает местоположение номера для заданного типа или null, если
местоположение не определено и действие с номером следует отменить.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<INumberLocation> TryGetNumberLocationAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetNumberLocationAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberLocation)
C++ __Копировать
     public:
    virtual ValueTask<INumberLocation^> TryGetNumberLocationAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetNumberLocationAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberLocation> 
    override TryGetNumberLocationAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberLocation> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
     Тип номера, для которого требуется определить местоположение номера в заданном контексте действия. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)>  
Местоположение номера для заданного типа или null, если местоположение не
определено и действие с номером следует отменить.
#### Реализации
[INumberBuilder.TryGetNumberLocationAsync(INumberContext,
NumberTypeDescriptor,
CancellationToken)](M_Tessa_Cards_Numbers_INumberBuilder_TryGetNumberLocationAsync.htm)  
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
