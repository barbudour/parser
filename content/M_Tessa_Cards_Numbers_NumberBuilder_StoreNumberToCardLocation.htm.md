# NumberBuilder.StoreNumberToCardLocation - метод
Сохраняет номер в карточку в место, указанное в параметре cardLocation.
Возвращает false, если сохранить номер не удалось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected bool StoreNumberToCardLocation(
    	INumberContext context,
    	INumberObject number,
    	CardNumberLocation cardLocation,
    	NumberStoreMode storeMode = NumberStoreMode.WithNotification
    )
VB __Копировать
     Protected Function StoreNumberToCardLocation ( 
    	context As INumberContext,
    	number As INumberObject,
    	cardLocation As CardNumberLocation,
    	Optional storeMode As NumberStoreMode = NumberStoreMode.WithNotification
    ) As Boolean
C++ __Копировать
     protected:
    bool StoreNumberToCardLocation(
    	INumberContext^ context, 
    	INumberObject^ number, 
    	CardNumberLocation^ cardLocation, 
    	NumberStoreMode storeMode = NumberStoreMode::WithNotification
    )
F# __Копировать
     member StoreNumberToCardLocation : 
            context : INumberContext * 
            number : INumberObject * 
            cardLocation : CardNumberLocation * 
            ?storeMode : NumberStoreMode 
    (* Defaults:
            let _storeMode = defaultArg storeMode NumberStoreMode.WithNotification
    *)
    -> bool 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
    Сохраняемый номер.
cardLocation
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm)
     Местоположение номера в карточке. Может быть равно null, в этом случае метод возвращает false. 
storeMode [NumberStoreMode](T_Tessa_Cards_Numbers_NumberStoreMode.htm)
(Optional)
    Способ сохранения номера в карточке.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если номер успешно сохранён; false, если сохранение было отменено.
## __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
