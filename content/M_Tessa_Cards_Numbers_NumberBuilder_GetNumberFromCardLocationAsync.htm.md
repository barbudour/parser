# NumberBuilder.GetNumberFromCardLocationAsync - метод
Возвращает номер, расположенный в карточке в месте, указанном в параметре
cardLocation, или пустой номер, если номер пуст или его не удалось получить.
Метод не возвращает null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected ValueTask<INumberObject> GetNumberFromCardLocationAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	CardNumberLocation cardLocation,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Function GetNumberFromCardLocationAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	cardLocation As CardNumberLocation,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     protected:
    ValueTask<INumberObject^> GetNumberFromCardLocationAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	CardNumberLocation^ cardLocation, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetNumberFromCardLocationAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            cardLocation : CardNumberLocation * 
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
cardLocation
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm)
     Местоположение номера в карточке. Может быть равно null, в этом случае метод возвращает пустой номер. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Номер, расположенный в карточке в месте, указанном в параметре cardLocation,
или пустой номер, если номер пуст или его не удалось получить. Метод не
возвращает null.
## __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
