# CardHelper.GetCardFileTypes - метод
Получение набора типов файлов [IFileType](T_Tessa_Files_IFileType.htm) по
типам карточек [CardType](T_Tessa_Cards_CardType.htm), полученным из
метаданных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ICollection<IFileType> GetCardFileTypes(
    	IEnumerable<CardType> fileTypes
    )
VB __Копировать
     Public Shared Function GetCardFileTypes ( 
    	fileTypes As IEnumerable(Of CardType)
    ) As ICollection(Of IFileType)
C++ __Копировать
     public:
    static ICollection<IFileType^>^ GetCardFileTypes(
    	IEnumerable<CardType^>^ fileTypes
    )
F# __Копировать
     static member GetCardFileTypes : 
            fileTypes : IEnumerable<CardType> -> ICollection<IFileType> 
#### Параметры
fileTypes
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardType](T_Tessa_Cards_CardType.htm)>
    Типы карточек, относящиеся к файлам.
#### Возвращаемое значение
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileType](T_Tessa_Files_IFileType.htm)>  
Типы файлов в карточке.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
