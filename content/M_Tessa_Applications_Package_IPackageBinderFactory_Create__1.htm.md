# IPackageBinderFactory.Create<T> \- метод
Предоставляет объект типа T
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     T Create<T>()
    where T : IApplicationPackageBinder
VB __Копировать
     Function Create(Of T As IApplicationPackageBinder) As T
C++ __Копировать
    generic<typename T>
    where T : IApplicationPackageBinder
    T Create()
F# __Копировать
     abstract Create : unit -> 'T  when 'T : IApplicationPackageBinder
#### Параметры типа
T
     Тип запрашиваемого объекта 
#### Возвращаемое значение
T  
Запрошенный объект
## __См. также
#### Ссылки
[IPackageBinderFactory -
](T_Tessa_Applications_Package_IPackageBinderFactory.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
