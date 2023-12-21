# AsyncFuncMergeResultItem<T, TArgs> \- конструктор
Создает объект результата слияния
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AsyncFuncMergeResultItem(
    	Func<T, TArgs, CancellationToken, ValueTask> func,
    	TArgs args = null
    )
VB __Копировать
     Public Sub New ( 
    	func As Func(Of T, TArgs, CancellationToken, ValueTask),
    	Optional args As TArgs = Nothing
    )
C++ __Копировать
     public:
    AsyncFuncMergeResultItem(
    	Func<T, TArgs, CancellationToken, ValueTask>^ func, 
    	TArgs args = nullptr
    )
F# __Копировать
     new : 
            func : Func<'T, 'TArgs, CancellationToken, ValueTask> * 
            ?args : 'TArgs 
    (* Defaults:
            let _args = defaultArg args null
    *)
    -> AsyncFuncMergeResultItem
#### Параметры
func
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[T](T_Tessa_SmartMerge_AsyncFuncMergeResultItem_2.htm),
[TArgs](T_Tessa_SmartMerge_AsyncFuncMergeResultItem_2.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
    Функция, которая будет применена к объекту слияния
args [TArgs](T_Tessa_SmartMerge_AsyncFuncMergeResultItem_2.htm) (Optional)
    Аргументы функции
##  __См. также
#### Ссылки
[AsyncFuncMergeResultItem<T, TArgs> \-
](T_Tessa_SmartMerge_AsyncFuncMergeResultItem_2.htm)
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
