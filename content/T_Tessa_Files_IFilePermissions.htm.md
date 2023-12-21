# IFilePermissions - интерфейс
Разрешения, определяющие возможности, доступные пользователю при работе с
файлом.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFilePermissions : ICloneable, 
    	INotifyPropertyChanged, ISealable
VB __Копировать
     Public Interface IFilePermissions
    	Inherits ICloneable, INotifyPropertyChanged, ISealable
C++ __Копировать
     public interface class IFilePermissions : ICloneable, 
    	INotifyPropertyChanged, ISealable
F# __Копировать
     type IFilePermissions = 
        interface
            interface ICloneable
            interface INotifyPropertyChanged
            interface ISealable
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[CanCopy](P_Tessa_Files_IFilePermissions_CanCopy.htm)| Признак того, что файл
можно скопировать.  
---|---  
[CanEdit](P_Tessa_Files_IFilePermissions_CanEdit.htm)| Признак того, что
контент файла можно редактировать.  
[CanModifyCategory](P_Tessa_Files_IFilePermissions_CanModifyCategory.htm)|
Признак того, что категория файла может быть изменена.  
[CanModifyName](P_Tessa_Files_IFilePermissions_CanModifyName.htm)| Признак
того, что файл можно переименовать.  
[CanModifyProperties](P_Tessa_Files_IFilePermissions_CanModifyProperties.htm)|
Признак того, что свойства файла могут быть изменены.  
[CanModifyType](P_Tessa_Files_IFilePermissions_CanModifyType.htm)| Признак
того, что тип файла может быть изменён.  
[CanRemove](P_Tessa_Files_IFilePermissions_CanRemove.htm)| Признак того, что
файл можно удалить.  
[CanRemoveSignatures](P_Tessa_Files_IFilePermissions_CanRemoveSignatures.htm)|
Признак того, что пользователь может удалить подписи для любой версии файла.
Как правило, такое действие доступно только администратору.  
[CanReplace](P_Tessa_Files_IFilePermissions_CanReplace.htm)| Признак того, что
контент файла можно заменить.  
[CanSign](P_Tessa_Files_IFilePermissions_CanSign.htm)|  Признак того, что файл
можно подписать. Подписывается всегда последняя версия файла.  
[CanUseSignatures](P_Tessa_Files_IFilePermissions_CanUseSignatures.htm)|
Признак того, что для файла разрешено использовать подписи, т.е. подписывать,
удалять, проверять или просматривать подписи.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __Методы
[Clone](M_Tessa_Files_IFilePermissions_Clone.htm)|  Создаёт полную копию
текущего объекта. Флаг защиты от изменений [Tessa.Platform.ISealable.Seal] в
созданной копии сбрасывается.  
---|---  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SetAsync](M_Tessa_Files_IFilePermissions_SetAsync.htm)| Устанавливает все
разрешения текущего объекта равными разрешениям в заданном объекте.  
[SetCanCopyAsync](M_Tessa_Files_IFilePermissions_SetCanCopyAsync.htm)|
Устанавливает признак того, что файл можно скопировать.  
[SetCanEditAsync](M_Tessa_Files_IFilePermissions_SetCanEditAsync.htm)|
Устанавливает признак того, что контент файла можно редактировать.  
[SetCanModifyCategoryAsync](M_Tessa_Files_IFilePermissions_SetCanModifyCategoryAsync.htm)|
Устанавливает признак того, что категория файла может быть изменена.  
[SetCanModifyNameAsync](M_Tessa_Files_IFilePermissions_SetCanModifyNameAsync.htm)|
Устанавливает признак того, что файл можно переименовать.  
[SetCanModifyPropertiesAsync](M_Tessa_Files_IFilePermissions_SetCanModifyPropertiesAsync.htm)|
Устанавливает признак того, что свойства файла могут быть изменены.  
[SetCanModifyTypeAsync](M_Tessa_Files_IFilePermissions_SetCanModifyTypeAsync.htm)|
Устанавливает признак того, что тип файла может быть изменён.  
[SetCanRemoveAsync](M_Tessa_Files_IFilePermissions_SetCanRemoveAsync.htm)|
Устанавливает признак того, что файл можно удалить.  
[SetCanRemoveSignaturesAsync](M_Tessa_Files_IFilePermissions_SetCanRemoveSignaturesAsync.htm)|
Устанавливает признак того, что пользователь может удалить подписи для любой
версии файла. Как правило, такое действие доступно только администратору.  
[SetCanReplaceAsync](M_Tessa_Files_IFilePermissions_SetCanReplaceAsync.htm)|
Устанавливает признак того, что контент файла можно заменить.  
[SetCanSignAsync](M_Tessa_Files_IFilePermissions_SetCanSignAsync.htm)|
Устанавливает признак того, что файл можно подписать. Подписывается всегда
последняя версия файла.  
[SetCanUseSignaturesAsync](M_Tessa_Files_IFilePermissions_SetCanUseSignaturesAsync.htm)|
Устанавливает признак того, что для файла разрешено использовать подписи, т.е.
подписывать, удалять, проверять или просматривать подписи.  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
