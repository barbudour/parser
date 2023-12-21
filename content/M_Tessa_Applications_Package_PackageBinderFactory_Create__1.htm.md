# PackageBinderFactory.Create<T> \- метод
Предоставляет объект типа T
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public T Create<T>()
    where T : IApplicationPackageBinder
VB __Копировать
     Public Function Create(Of T As IApplicationPackageBinder) As T
C++ __Копировать
     public:
    generic<typename T>
    where T : IApplicationPackageBinder
    virtual T Create() sealed
F# __Копировать
     abstract Create : unit -> 'T  when 'T : IApplicationPackageBinder
    override Create : unit -> 'T  when 'T : IApplicationPackageBinder
#### Параметры типа
T
     Тип запрашиваемого объекта 
#### Возвращаемое значение
T  
Запрошенный объект
#### Реализации
[IPackageBinderFactory.Create<T>()](M_Tessa_Applications_Package_IPackageBinderFactory_Create__1.htm)  
##  __См. также
#### Ссылки
[PackageBinderFactory -
](T_Tessa_Applications_Package_PackageBinderFactory.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
