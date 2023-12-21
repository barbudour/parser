# FileBuilder.ContentCreationType - перечисление
Способ создания контента.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected enum ContentCreationType
VB __Копировать
     Protected Enumeration ContentCreationType
C++ __Копировать
     protected enum class ContentCreationType
F# __Копировать
     type ContentCreationType
##  __Члены
Undefined| 0|  Способ создания не был определён. При этом контент не
создаётся.  
---|---|---  
Path| 1|  Контент создаётся по заданному пути к файлу
[ContentPath](P_Tessa_Files_FileBuilder_ContentPath.htm).  
Stream| 2|  Контент создаётся по заданному потоку
[ContentStream](P_Tessa_Files_FileBuilder_ContentStream.htm).  
Action| 3|  Контент создаётся по заданному методу изменения контента
[ContentActionAsync](P_Tessa_Files_FileBuilder_ContentActionAsync.htm).  
Factory| 4|  Контент создаётся по заданному методу создания контента
[ContentFactoryAsync](P_Tessa_Files_FileBuilder_ContentFactoryAsync.htm).  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
