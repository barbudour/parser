# LazyResolvePolicy(Lazy<IExtension>) - конструктор
Создаёт экземпляр класса с указанием отложенной ссылки на экземпляр
расширения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public LazyResolvePolicy(
    	Lazy<IExtension> instanceLazy
    )
VB __Копировать
     Public Sub New ( 
    	instanceLazy As Lazy(Of IExtension)
    )
C++ __Копировать
     public:
    LazyResolvePolicy(
    	Lazy<IExtension^>^ instanceLazy
    )
F# __Копировать
     new : 
            instanceLazy : Lazy<IExtension> -> LazyResolvePolicy
#### Параметры
instanceLazy
[Lazy](https://learn.microsoft.com/dotnet/api/system.lazy-1)<[IExtension](T_Tessa_Extensions_IExtension.htm)>
    Отложенная ссылка на экземпляр расширения.
##  __См. также
#### Ссылки
[LazyResolvePolicy - ](T_Tessa_Extensions_LazyResolvePolicy.htm)
[LazyResolvePolicy -
перегрузка](Overload_Tessa_Extensions_LazyResolvePolicy__ctor.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
