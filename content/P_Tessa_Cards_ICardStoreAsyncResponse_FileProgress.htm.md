# ICardStoreAsyncResponse.FileProgress - свойство
Прогресс операции, вычисляемый как отношение суммарного количества уже
загруженных байт, относящихся к файлам, к суммарному размеру всех файлов,
которые требуется загрузить. Не учитывает размеры заголовка и запроса на
сохранение карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     double FileProgress { get; }
VB __Копировать
     ReadOnly Property FileProgress As Double
    	Get
C++ __Копировать
    property double FileProgress {
    	double get ();
    }
F# __Копировать
     abstract FileProgress : float with get
#### Значение свойства
[Double](https://learn.microsoft.com/dotnet/api/system.double)
##  __См. также
#### Ссылки
[ICardStoreAsyncResponse - ](T_Tessa_Cards_ICardStoreAsyncResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
