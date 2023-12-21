# CardHeader.GetOrderedFiles - метод
Возвращает упорядоченное перечисление объектов, содержащих информацию о
содержимом файлов в потоке.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IEnumerable<CardHeaderFile> GetOrderedFiles()
VB __Копировать
     Public Function GetOrderedFiles As IEnumerable(Of CardHeaderFile)
C++ __Копировать
     public:
    IEnumerable<CardHeaderFile^>^ GetOrderedFiles()
F# __Копировать
     member GetOrderedFiles : unit -> IEnumerable<CardHeaderFile> 
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardHeaderFile](T_Tessa_Cards_ComponentModel_CardHeaderFile.htm)>  
Упорядоченное перечисление объектов, содержащих информацию о содержимом файлов
в потоке.
##  __Заметки
Метод следует использовать для определения порядка следования файлов в потоке.
Объекты с информацией о файлах упорядочиваются сначала по
[Order](P_Tessa_Cards_ComponentModel_CardHeaderFile_Order.htm), затем по
[ID](P_Tessa_Cards_ComponentModel_CardHeaderFile_ID.htm).
## __См. также
#### Ссылки
[CardHeader - ](T_Tessa_Cards_ComponentModel_CardHeader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
