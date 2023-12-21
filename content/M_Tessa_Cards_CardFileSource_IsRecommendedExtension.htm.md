# CardFileSource.IsRecommendedExtension - метод
Возвращает признак того, что заданное расширение файла является рекомендуемым
для использования совместно с этим источником файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsRecommendedExtension(
    	string fileExtension
    )
VB __Копировать
     Public Function IsRecommendedExtension ( 
    	fileExtension As String
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsRecommendedExtension(
    	String^ fileExtension
    ) sealed
F# __Копировать
     abstract IsRecommendedExtension : 
            fileExtension : string -> bool 
    override IsRecommendedExtension : 
            fileExtension : string -> bool 
#### Параметры
fileExtension [String](https://learn.microsoft.com/dotnet/api/system.string)
     Расширение файла с ведущей точкой. Может быть равно null. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданное расширение файла является рекомендуемым для использования
совместно с этим источником файлов; false в противном случае.
#### Реализации
[ICardFileSource.IsRecommendedExtension(String)](M_Tessa_Cards_ICardFileSource_IsRecommendedExtension.htm)  
##  __См. также
#### Ссылки
[CardFileSource - ](T_Tessa_Cards_CardFileSource.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
