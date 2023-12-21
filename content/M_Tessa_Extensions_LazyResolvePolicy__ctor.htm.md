# LazyResolvePolicy(Func<IExtension>) - конструктор
Создаёт экземпляр класса с указанием функции, возвращающей ссылку на экземпляр
расширения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public LazyResolvePolicy(
    	Func<IExtension> instanceFunc
    )
VB __Копировать
     Public Sub New ( 
    	instanceFunc As Func(Of IExtension)
    )
C++ __Копировать
     public:
    LazyResolvePolicy(
    	Func<IExtension^>^ instanceFunc
    )
F# __Копировать
     new : 
            instanceFunc : Func<IExtension> -> LazyResolvePolicy
#### Параметры
instanceFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IExtension](T_Tessa_Extensions_IExtension.htm)>
     Функция, возвращающая ссылку на экземпляр расширения. Функция используется только при первом получении экземпляра, но есть вероятность, что она будет вызвана несколько раз из различных потоков. 
## __Заметки
Если для функции instanceFunc требуется настройка потокобезопасности или не
более одного вызова, то используйте перегрузку конструктора, принимающую
[Lazy<T>](https://learn.microsoft.com/dotnet/api/system.lazy-1) .
## __См. также
#### Ссылки
[LazyResolvePolicy - ](T_Tessa_Extensions_LazyResolvePolicy.htm)
[LazyResolvePolicy -
перегрузка](Overload_Tessa_Extensions_LazyResolvePolicy__ctor.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
