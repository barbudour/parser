# FileNotificationType - перечисление
Тип уведомления, которое отправляется для файла
[IFile](T_Tessa_Files_IFile.htm) посредством
[IFileSource](T_Tessa_Files_IFileSource.htm) во внешнюю подсистему.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum FileNotificationType
VB __Копировать
     Public Enumeration FileNotificationType
C++ __Копировать
     public enum class FileNotificationType
F# __Копировать
     type FileNotificationType
##  __Члены
Added| 0|  Файл был добавлен.  
---|---|---  
AddedVirtual| 1|  Файл был добавлен как виртуальный, т.е. не отмечен как
создаваемый при сохранении. Обычно таким образом добавляются виртуальные файлы
при загрузке карточки. Источник файлов
[IFileSource](T_Tessa_Files_IFileSource.htm) может не делать различия между
Added и AddedVirtual, но для стандартного источника для карточек отличие в
состоянии созданного файла и в флаге
[IsVirtual](P_Tessa_Cards_CardFile_IsVirtual.htm).  
Removed| 2|  Файл был удалён.  
Reverted| 3|  Контент и имя файла были восстановлены после редактирования
ContentModified или замены ContentReplaced.  
CategoryModified| 4|  Категория файла была изменена. Отражает изменение
значения свойства [Category](P_Tessa_Files_IFile_Category.htm).  
NameModified| 5|  Файл был переименован. Отражает изменение значения свойства
[Name](P_Tessa_Files_IFileObject_Name.htm).  
ContentModified| 6|  Контент файла был изменён. Отражает изменение контента
методом [!:IFileContent.Set].  
ContentReplaced| 7|  Контент файла был заменён. Отражает замену контента
методом [!:IFileContent.Set] с созданием новой версии.  
OriginModified| 8|  Был переназначен файл, из которого выполнялась копия
текущего файла. Отражает изменение значения свойства
[Origin](P_Tessa_Files_IFile_Origin.htm)/  
OptionsModified| 9|  Были изменены опции файла. Обычно вызывается из
расширений. Отражает изменение значения свойства [!:IFile.Options]/  
NewVersionTagsModified| 10|  Были изменены теги для создаваемой версии файла.
Обычно вызывается из расширений. Отражает изменение значения свойства
[NewVersionTags](P_Tessa_Files_IFile_NewVersionTags.htm)/  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
