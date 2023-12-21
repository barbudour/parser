# NumberBuilder.TryGetNumberEffectiveLocationCoreAsync - метод
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<INumberLocation> TryGetNumberEffectiveLocationCoreAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	INumberLocation location,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function TryGetNumberEffectiveLocationCoreAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	location As INumberLocation,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberLocation)
C++ __Копировать
     protected:
    virtual ValueTask<INumberLocation^> TryGetNumberEffectiveLocationCoreAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	INumberLocation^ location, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetNumberEffectiveLocationCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            location : INumberLocation * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberLocation> 
    override TryGetNumberEffectiveLocationCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            location : INumberLocation * 
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
    Тип номера.
location [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
    Местоположение номера, по которому требуется получить эффективное местоположение.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)>  
Эффективное местоположение для заданного местоположение или null, если
эффективное местоположение недоступно и следует использовать заданное
местоположение location.
## __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
