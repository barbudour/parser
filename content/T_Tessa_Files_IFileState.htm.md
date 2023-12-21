# IFileState - интерфейс
Состояние файла на определённый момент времени.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileState
VB __Копировать
     Public Interface IFileState
C++ __Копировать
     public interface class IFileState
F# __Копировать
     type IFileState = interface end
##  __Свойства
[Category](P_Tessa_Files_IFileState_Category.htm)|  Категория файла или null,
если файл не имеет категории.  
---|---  
[Name](P_Tessa_Files_IFileState_Name.htm)| Имя файла.  
[Origin](P_Tessa_Files_IFileState_Origin.htm)|  Исходный файл, из которого был
скопирован текущий файл, или null, если текущий файл не был скопирован.  
[Type](P_Tessa_Files_IFileState_Type.htm)| Тип файла.  
##  __Методы
[IsDependantFileProperty](M_Tessa_Files_IFileState_IsDependantFileProperty.htm)|
Возвращает признак того, что свойство файла с заданным именем зависит от его
состояния, т.е. изменение свойства также изменит и состояние файла.  
---|---  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
