# NumberHelper.GetContainer<T> \- метод
Возвращает объект-контейнер, позволяющий получить результат ссылочного типа
для заданного действия с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static NumberEventContainer<T> GetContainer<T>(
    	Func<INumberContext, CancellationToken, Task<T>> numberEventFuncAsync
    )
    where T : class
VB __Копировать
     Public Shared Function GetContainer(Of T As Class) ( 
    	numberEventFuncAsync As Func(Of INumberContext, CancellationToken, Task(Of T))
    ) As NumberEventContainer(Of T)
C++ __Копировать
     public:
    generic<typename T>
    where T : ref class
    static NumberEventContainer<T>^ GetContainer(
    	Func<INumberContext^, CancellationToken, Task<T>^>^ numberEventFuncAsync
    )
F# __Копировать
     static member GetContainer : 
            numberEventFuncAsync : Func<INumberContext, CancellationToken, Task<'T>> -> NumberEventContainer<'T>  when 'T : not struct
#### Параметры
numberEventFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<T>>
     Действие с номером, принимающее в параметре контекст действия [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm), отличный от null, и возвращающее ссылочный результат действия. Если возвращается null, то действие считается неудачным. 
#### Параметры типа
T
    Ссылочный тип результата действия с номером.
#### Возвращаемое значение
[NumberEventContainer](T_Tessa_Cards_Numbers_NumberEventContainer_1.htm)<T>  
Созданный объект.
##  __См. также
#### Ссылки
[NumberHelper - ](T_Tessa_Cards_Numbers_NumberHelper.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
