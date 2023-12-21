# CardSchemeSerializableObject.RemoveUnknownFromCollection<T> \- метод
Выполняет удаление из коллекции элементов, определённых как неизвестные, с
записью сообщения по таким элементам в результат валидации.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static bool RemoveUnknownFromCollection<T>(
    	ICollection<T> items,
    	IValidationResultBuilder validationResult,
    	Func<T, bool> isUnknownFunc,
    	Action<T, IValidationResultBuilder> validateUnknownAction
    )
VB __Копировать
     Protected Shared Function RemoveUnknownFromCollection(Of T) ( 
    	items As ICollection(Of T),
    	validationResult As IValidationResultBuilder,
    	isUnknownFunc As Func(Of T, Boolean),
    	validateUnknownAction As Action(Of T, IValidationResultBuilder)
    ) As Boolean
C++ __Копировать
     protected:
    generic<typename T>
    static bool RemoveUnknownFromCollection(
    	ICollection<T>^ items, 
    	IValidationResultBuilder^ validationResult, 
    	Func<T, bool>^ isUnknownFunc, 
    	Action<T, IValidationResultBuilder^>^ validateUnknownAction
    )
F# __Копировать
     static member RemoveUnknownFromCollection : 
            items : ICollection<'T> * 
            validationResult : IValidationResultBuilder * 
            isUnknownFunc : Func<'T, bool> * 
            validateUnknownAction : Action<'T, IValidationResultBuilder> -> bool 
#### Параметры
items
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>
     Коллекция проверяемых элементов. Значение null расценивается как пустая коллекция. 
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий валидацию.
isUnknownFunc [Func](https://learn.microsoft.com/dotnet/api/system.func-2)<T,
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Функция, определяющая, является ли переданный в качестве параметра элемент неизвестным. 
validateUnknownAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-2)<T,
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)>
     Метод, записывающий сообщение по первому параметру, который был определён как неизвестный элемент, во второй параметр. 
#### Параметры типа
T
    Тип элементов в коллекции.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если был обнаружен хотя бы один элемент коллекции, являющийся
неизвестным; false в противном случае.
## __См. также
#### Ссылки
[CardSchemeSerializableObject -
](T_Tessa_Cards_CardSchemeSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
