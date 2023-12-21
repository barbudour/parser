# IFileCategory - интерфейс
Категория файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileCategory : IEquatable<IFileCategory>
VB __Копировать
     Public Interface IFileCategory
    	Inherits IEquatable(Of IFileCategory)
C++ __Копировать
     public interface class IFileCategory : IEquatable<IFileCategory^>
F# __Копировать
     type IFileCategory = 
        interface
            interface IEquatable<IFileCategory>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileCategory>
##  __Свойства
[Caption](P_Tessa_Files_IFileCategory_Caption.htm)|  Отображаемое имя
категории файла, которое видит пользователь. Не может быть равно null, пустой
строке или строке, состоящей из пробелов.  
---|---  
[ID](P_Tessa_Files_IFileCategory_ID.htm)|  Уникальный идентификатор категории
файла или null, если категория не имеет идентификатора.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileCategory>)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
