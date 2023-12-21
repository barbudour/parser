# IFileTag - интерфейс
Тег, связанный с версией файла. Например, признак того, что размер содержимого
файла трактуется как большой файл, поэтому файл не копируется во временную
папку.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileTag : IEquatable<IFileTag>, 
    	ISealable
VB __Копировать
     Public Interface IFileTag
    	Inherits IEquatable(Of IFileTag), ISealable
C++ __Копировать
     public interface class IFileTag : IEquatable<IFileTag^>, 
    	ISealable
F# __Копировать
     type IFileTag = 
        interface
            interface IEquatable<IFileTag>
            interface ISealable
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileTag>, [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[Info](P_Tessa_Files_IFileTag_Info.htm)| Дополнительная информация для
расширений или null, если информация не требуется.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Key](P_Tessa_Files_IFileTag_Key.htm)| Ключ, уникально идентифицирующий тег.
При сравнении ключей обычно не учитывается регистр символов.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileTag>)  
---|---  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
