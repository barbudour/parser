# IFileContainerPermissions - интерфейс
Разрешения, определяющие возможности, доступные пользователю при работе с
контейнером файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileContainerPermissions : ICloneable, 
    	INotifyPropertyChanged, ISealable
VB __Копировать
     Public Interface IFileContainerPermissions
    	Inherits ICloneable, INotifyPropertyChanged, ISealable
C++ __Копировать
     public interface class IFileContainerPermissions : ICloneable, 
    	INotifyPropertyChanged, ISealable
F# __Копировать
     type IFileContainerPermissions = 
        interface
            interface ICloneable
            interface INotifyPropertyChanged
            interface ISealable
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[CanAdd](P_Tessa_Files_IFileContainerPermissions_CanAdd.htm)| Признак того,
что файл можно добавить.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __Методы
[Clone](M_Tessa_Files_IFileContainerPermissions_Clone.htm)|  Создаёт полную
копию текущего объекта. Флаг защиты от изменений
[Tessa.Platform.ISealable.Seal] в созданной копии сбрасывается.  
---|---  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SetAsync](M_Tessa_Files_IFileContainerPermissions_SetAsync.htm)|
Устанавливает все разрешения текущего объекта равными разрешениям в заданном
объекте.  
[SetCanAddAsync](M_Tessa_Files_IFileContainerPermissions_SetCanAddAsync.htm)|
Устанавливает признак того, что файл можно добавить.  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
[ApplyFromAsync](M_Tessa_Cards_CardExtensions_ApplyFromAsync.htm)|
Устанавливает разрешения, связанные с контейнером файлов, по разрешениям,
заданным в карточке.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
