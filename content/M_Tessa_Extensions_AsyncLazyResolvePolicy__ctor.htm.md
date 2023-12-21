# AsyncLazyResolvePolicy(Func<Task<IExtension>>) - конструктор
Создаёт экземпляр класса с указанием функции, возвращающей ссылку на экземпляр
расширения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AsyncLazyResolvePolicy(
    	Func<Task<IExtension>> instanceFuncAsync
    )
VB __Копировать
     Public Sub New ( 
    	instanceFuncAsync As Func(Of Task(Of IExtension))
    )
C++ __Копировать
     public:
    AsyncLazyResolvePolicy(
    	Func<Task<IExtension^>^>^ instanceFuncAsync
    )
F# __Копировать
     new : 
            instanceFuncAsync : Func<Task<IExtension>> -> AsyncLazyResolvePolicy
#### Параметры
instanceFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IExtension](T_Tessa_Extensions_IExtension.htm)>>
     Функция, возвращающая ссылку на экземпляр расширения. Функция используется только при первом получении экземпляра, но есть вероятность, что она будет вызвана несколько раз из различных потоков. 
## __Заметки
Если для функции instanceFuncAsync требуется настройка потокобезопасности или
не более одного вызова, то используйте перегрузку конструктора, принимающую
[Lazy<T>](https://learn.microsoft.com/dotnet/api/system.lazy-1) .
## __См. также
#### Ссылки
[AsyncLazyResolvePolicy - ](T_Tessa_Extensions_AsyncLazyResolvePolicy.htm)
[AsyncLazyResolvePolicy -
перегрузка](Overload_Tessa_Extensions_AsyncLazyResolvePolicy__ctor.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
