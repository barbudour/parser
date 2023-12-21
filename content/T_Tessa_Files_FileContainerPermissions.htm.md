# FileContainerPermissions - класс
Разрешения, определяющие возможности, доступные пользователю при работе с
контейнером файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileContainerPermissions : NotificationObject, 
    	IFileContainerPermissions, ICloneable, INotifyPropertyChanged, ISealable
VB __Копировать
     Public Class FileContainerPermissions
    	Inherits NotificationObject
    	Implements IFileContainerPermissions, ICloneable, INotifyPropertyChanged, ISealable
C++ __Копировать
     public ref class FileContainerPermissions : public NotificationObject, 
    	IFileContainerPermissions, ICloneable, INotifyPropertyChanged, ISealable
F# __Копировать
     type FileContainerPermissions = 
        class
            inherit NotificationObject
            interface IFileContainerPermissions
            interface ICloneable
            interface INotifyPropertyChanged
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ FileContainerPermissions
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IFileContainerPermissions](T_Tessa_Files_IFileContainerPermissions.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[FileContainerPermissions()](M_Tessa_Files_FileContainerPermissions__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[FileContainerPermissions(IFileContainerPermissions)](M_Tessa_Files_FileContainerPermissions__ctor_1.htm)|
Создаёт экземпляр класса, копируя свойства из заданного объекта с
разрешениями.  
## __Свойства
[CanAdd](P_Tessa_Files_FileContainerPermissions_CanAdd.htm)| Признак того, что
файл можно добавить.  
---|---  
[Empty](P_Tessa_Files_FileContainerPermissions_Empty.htm)|  Полностью
отсутствующие разрешения. Подходят при открытии карточки в режиме только для
чтения. Свойства объекта нельзя изменять.  
[Full](P_Tessa_Files_FileContainerPermissions_Full.htm)|  Полностью заданные
разрешения. Подходит для полных прав на редактирование файлов в карточке.
Свойства объекта нельзя изменять.  
[IsSealed](P_Tessa_Files_FileContainerPermissions_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
##  __Методы
[Clone](M_Tessa_Files_FileContainerPermissions_Clone.htm)|  Создаёт полную
копию текущего объекта. Флаг защиты от изменений
[Tessa.Platform.ISealable.Seal] в созданной копии сбрасывается.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[Seal](M_Tessa_Files_FileContainerPermissions_Seal.htm)| Защищает объект от
изменений.  
[SetAsync](M_Tessa_Files_FileContainerPermissions_SetAsync.htm)| Устанавливает
все разрешения текущего объекта равными разрешениям в заданном объекте.  
[SetCanAddAsync](M_Tessa_Files_FileContainerPermissions_SetCanAddAsync.htm)|
Устанавливает признак того, что файл можно добавить.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
##  __Методы расширения
[ApplyFromAsync](M_Tessa_Cards_CardExtensions_ApplyFromAsync.htm)|
Устанавливает разрешения, связанные с контейнером файлов, по разрешениям,
заданным в карточке.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
